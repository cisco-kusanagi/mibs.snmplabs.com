#
# PySNMP MIB module NETASQ-AUTHUSERS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETASQ-AUTHUSERS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:08:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ntqUsers, = mibBuilder.importSymbols("NETASQ-SMI-MIB", "ntqUsers")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibIdentifier, Gauge32, Counter32, Counter64, ObjectIdentity, Unsigned32, IpAddress, ModuleIdentity, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "Gauge32", "Counter32", "Counter64", "ObjectIdentity", "Unsigned32", "IpAddress", "ModuleIdentity", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ntqAuthUsersTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 2, 1), )
if mibBuilder.loadTexts: ntqAuthUsersTable.setStatus('current')
ntqAuthUsersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1), ).setIndexNames((0, "NETASQ-AUTHUSERS-MIB", "ntqAuthUsersIPAddr"))
if mibBuilder.loadTexts: ntqAuthUsersEntry.setStatus('current')
ntqAuthUsersIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqAuthUsersIPAddr.setStatus('current')
ntqAuthUsersTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqAuthUsersTimeOut.setStatus('current')
ntqAuthUsersName = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqAuthUsersName.setStatus('current')
mibBuilder.exportSymbols("NETASQ-AUTHUSERS-MIB", ntqAuthUsersEntry=ntqAuthUsersEntry, ntqAuthUsersName=ntqAuthUsersName, ntqAuthUsersTimeOut=ntqAuthUsersTimeOut, ntqAuthUsersIPAddr=ntqAuthUsersIPAddr, ntqAuthUsersTable=ntqAuthUsersTable)
