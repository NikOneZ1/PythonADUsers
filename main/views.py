from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ldap3.core.exceptions import LDAPBindError
import json
from .utils import create_connection


class CreateADConn(APIView):
    def post(self, request):
        try:
            conn = create_connection(request.data['hostname'],
                                     request.data['port'],
                                     request.data['user'],
                                     request.data['password'])
        except LDAPBindError:
            return Response({'response': "Connection failed. Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        if conn:
            request.session['connection_data'] = request.data
            return Response({'response': "Connection created"}, status=status.HTTP_200_OK)
        return Response({'response': "Connection failed"}, status=status.HTTP_400_BAD_REQUEST)


class GetADUsers(APIView):
    def get(self, request):
        connection_data = request.session['connection_data']
        conn = create_connection(connection_data['hostname'],
                                 connection_data['port'],
                                 connection_data['user'],
                                 connection_data['password'])
        group = request.GET.get("group", "")
        if filter:
            print(f'{group}', '(objectclass=person)')
            conn.search(f'{group}', '(objectclass=person)')
        else:
            conn.search('', '(objectclass=person)')
        response_data = []
        for entry in conn.entries:
            response_data.append(json.loads(entry.entry_to_json()))
        return Response(response_data, status.HTTP_200_OK)
