#
# PySNMP MIB module ALCATEL-IND1-AL-SRV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-AL-SRV-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:01:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1ActiveLeaseSrvMIB, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1ActiveLeaseSrvMIB")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Bits, TimeTicks, Integer32, NotificationType, IpAddress, ModuleIdentity, Unsigned32, Counter32, MibIdentifier, Gauge32, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "TimeTicks", "Integer32", "NotificationType", "IpAddress", "ModuleIdentity", "Unsigned32", "Counter32", "MibIdentifier", "Gauge32", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString, DateAndTime, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "DateAndTime", "MacAddress")
alcatelIND1ActiveLeaseSrvMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1))
alcatelIND1ActiveLeaseSrvMIB.setRevisions(('2013-06-05 00:00',))
if mibBuilder.loadTexts: alcatelIND1ActiveLeaseSrvMIB.setLastUpdated('201306050000Z')
if mibBuilder.loadTexts: alcatelIND1ActiveLeaseSrvMIB.setOrganization('Alcatel - Architects Of An Internet World')
alcatelIND1ActiveLeaseSrvMIBNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 0))
if mibBuilder.loadTexts: alcatelIND1ActiveLeaseSrvMIBNotifications.setStatus('current')
alcatelIND1ActiveLeaseSrvMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 1))
if mibBuilder.loadTexts: alcatelIND1ActiveLeaseSrvMIBObjects.setStatus('current')
alcatelIND1ActiveLeaseSrvMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 2))
if mibBuilder.loadTexts: alcatelIND1ActiveLeaseSrvMIBConformance.setStatus('current')
alcatelIND1ActiveLeaseSrvMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1ActiveLeaseSrvMIBGroups.setStatus('current')
alcatelIND1ActiveLeaseSrvMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1ActiveLeaseSrvMIBCompliances.setStatus('current')
alaActiveLeaseSrvGlobalConfigStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaActiveLeaseSrvGlobalConfigStatus.setStatus('current')
alaActiveLeaseSrvGlobalRestart = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("restart", 2))).clone('inactive')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaActiveLeaseSrvGlobalRestart.setStatus('current')
alcatelIND1ActiveLeaseSrvMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-AL-SRV-MIB", "alaActiveLeaseSrvGlobalConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1ActiveLeaseSrvMIBCompliance = alcatelIND1ActiveLeaseSrvMIBCompliance.setStatus('current')
alaActiveLeaseSrvGlobalConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-AL-SRV-MIB", "alaActiveLeaseSrvGlobalConfigStatus"), ("ALCATEL-IND1-AL-SRV-MIB", "alaActiveLeaseSrvGlobalRestart"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaActiveLeaseSrvGlobalConfigGroup = alaActiveLeaseSrvGlobalConfigGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-AL-SRV-MIB", alcatelIND1ActiveLeaseSrvMIBCompliance=alcatelIND1ActiveLeaseSrvMIBCompliance, alcatelIND1ActiveLeaseSrvMIBCompliances=alcatelIND1ActiveLeaseSrvMIBCompliances, alaActiveLeaseSrvGlobalRestart=alaActiveLeaseSrvGlobalRestart, alcatelIND1ActiveLeaseSrvMIB=alcatelIND1ActiveLeaseSrvMIB, alcatelIND1ActiveLeaseSrvMIBGroups=alcatelIND1ActiveLeaseSrvMIBGroups, alcatelIND1ActiveLeaseSrvMIBObjects=alcatelIND1ActiveLeaseSrvMIBObjects, alaActiveLeaseSrvGlobalConfigStatus=alaActiveLeaseSrvGlobalConfigStatus, PYSNMP_MODULE_ID=alcatelIND1ActiveLeaseSrvMIB, alaActiveLeaseSrvGlobalConfigGroup=alaActiveLeaseSrvGlobalConfigGroup, alcatelIND1ActiveLeaseSrvMIBConformance=alcatelIND1ActiveLeaseSrvMIBConformance, alcatelIND1ActiveLeaseSrvMIBNotifications=alcatelIND1ActiveLeaseSrvMIBNotifications)
