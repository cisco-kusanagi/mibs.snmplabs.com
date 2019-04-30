#
# PySNMP MIB module ALCATEL-IND1-MSG-SRV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-MSG-SRV-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:02:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1MsgSrvMIB, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1MsgSrvMIB")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, NotificationType, Integer32, Unsigned32, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, Counter32, Bits, Gauge32, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Integer32", "Unsigned32", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "Counter32", "Bits", "Gauge32", "ObjectIdentity", "iso")
MacAddress, DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "DateAndTime", "TextualConvention")
alcatelIND1MsgSrvMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1))
alcatelIND1MsgSrvMIB.setRevisions(('2013-06-05 00:00',))
if mibBuilder.loadTexts: alcatelIND1MsgSrvMIB.setLastUpdated('201306050000Z')
if mibBuilder.loadTexts: alcatelIND1MsgSrvMIB.setOrganization('Alcatel - Architects Of An Internet World')
alcatelIND1MsgSrvMIBNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 0))
if mibBuilder.loadTexts: alcatelIND1MsgSrvMIBNotifications.setStatus('current')
alcatelIND1MsgSrvMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 1))
if mibBuilder.loadTexts: alcatelIND1MsgSrvMIBObjects.setStatus('current')
alcatelIND1MsgSrvMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 2))
if mibBuilder.loadTexts: alcatelIND1MsgSrvMIBConformance.setStatus('current')
alcatelIND1MsgSrvMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1MsgSrvMIBGroups.setStatus('current')
alcatelIND1MsgSrvMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1MsgSrvMIBCompliances.setStatus('current')
alaMsgSrvGlobalConfigStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaMsgSrvGlobalConfigStatus.setStatus('current')
alaMsgSrvGlobalRestart = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("restart", 2))).clone('inactive')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaMsgSrvGlobalRestart.setStatus('current')
alcatelIND1MsgSrvMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-MSG-SRV-MIB", "alaMsgSrvGlobalConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1MsgSrvMIBCompliance = alcatelIND1MsgSrvMIBCompliance.setStatus('current')
alaMsgSrvGlobalConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-MSG-SRV-MIB", "alaMsgSrvGlobalConfigStatus"), ("ALCATEL-IND1-MSG-SRV-MIB", "alaMsgSrvGlobalRestart"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaMsgSrvGlobalConfigGroup = alaMsgSrvGlobalConfigGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-MSG-SRV-MIB", alcatelIND1MsgSrvMIBNotifications=alcatelIND1MsgSrvMIBNotifications, alcatelIND1MsgSrvMIBCompliances=alcatelIND1MsgSrvMIBCompliances, alcatelIND1MsgSrvMIBCompliance=alcatelIND1MsgSrvMIBCompliance, alaMsgSrvGlobalConfigGroup=alaMsgSrvGlobalConfigGroup, alcatelIND1MsgSrvMIBConformance=alcatelIND1MsgSrvMIBConformance, alcatelIND1MsgSrvMIB=alcatelIND1MsgSrvMIB, alcatelIND1MsgSrvMIBObjects=alcatelIND1MsgSrvMIBObjects, PYSNMP_MODULE_ID=alcatelIND1MsgSrvMIB, alcatelIND1MsgSrvMIBGroups=alcatelIND1MsgSrvMIBGroups, alaMsgSrvGlobalRestart=alaMsgSrvGlobalRestart, alaMsgSrvGlobalConfigStatus=alaMsgSrvGlobalConfigStatus)
