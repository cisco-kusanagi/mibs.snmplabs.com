#
# PySNMP MIB module Juniper-SUBSCRIBER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-SUBSCRIBER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:50:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniEnable, = mibBuilder.importSymbols("Juniper-TC", "JuniEnable")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, Unsigned32, IpAddress, Gauge32, ObjectIdentity, iso, Counter32, NotificationType, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "Unsigned32", "IpAddress", "Gauge32", "ObjectIdentity", "iso", "Counter32", "NotificationType", "MibIdentifier", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniSubscriberMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49))
juniSubscriberMIB.setRevisions(('2002-09-16 21:44', '2002-05-10 19:53', '2000-11-16 00:00',))
if mibBuilder.loadTexts: juniSubscriberMIB.setLastUpdated('200209162144Z')
if mibBuilder.loadTexts: juniSubscriberMIB.setOrganization('Juniper Networks, Inc.')
class JuniSubscrEncaps(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 19))
    namedValues = NamedValues(("ip", 0), ("bridgedEthernet", 19))

juniSubscrObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1))
juniSubscrLocal = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1))
juniSubscrLocalTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1), )
if mibBuilder.loadTexts: juniSubscrLocalTable.setStatus('current')
juniSubscrLocalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1), ).setIndexNames((0, "Juniper-SUBSCRIBER-MIB", "juniSubscrLocalIfIndex"), (0, "Juniper-SUBSCRIBER-MIB", "juniSubscrLocalEncaps"))
if mibBuilder.loadTexts: juniSubscrLocalEntry.setStatus('current')
juniSubscrLocalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniSubscrLocalIfIndex.setStatus('current')
juniSubscrLocalEncaps = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 2), JuniSubscrEncaps())
if mibBuilder.loadTexts: juniSubscrLocalEncaps.setStatus('current')
juniSubscrLocalControl = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ok", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSubscrLocalControl.setStatus('current')
juniSubscrLocalNamePrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 4), JuniEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSubscrLocalNamePrefix.setStatus('current')
juniSubscrLocalName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSubscrLocalName.setStatus('current')
juniSubscrLocalPasswordPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 6), JuniEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSubscrLocalPasswordPrefix.setStatus('current')
juniSubscrLocalPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSubscrLocalPassword.setStatus('current')
juniSubscrLocalDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSubscrLocalDomain.setStatus('current')
juniSubscrLocalAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 9), JuniEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSubscrLocalAuthentication.setStatus('current')
juniSubscriberMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4))
juniSubscriberMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 1))
juniSubscriberMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 2))
juniSubscriberCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 1, 1)).setObjects(("Juniper-SUBSCRIBER-MIB", "juniSubscriberLocalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSubscriberCompliance = juniSubscriberCompliance.setStatus('obsolete')
juniSubscriberCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 1, 2)).setObjects(("Juniper-SUBSCRIBER-MIB", "juniSubscriberLocalGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSubscriberCompliance2 = juniSubscriberCompliance2.setStatus('current')
juniSubscriberLocalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 2, 1)).setObjects(("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalControl"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalNamePrefix"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalName"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalPasswordPrefix"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalPassword"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalDomain"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSubscriberLocalGroup = juniSubscriberLocalGroup.setStatus('obsolete')
juniSubscriberLocalGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 2, 2)).setObjects(("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalControl"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalNamePrefix"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalName"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalPasswordPrefix"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalPassword"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalDomain"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalAuthentication"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSubscriberLocalGroup2 = juniSubscriberLocalGroup2.setStatus('current')
mibBuilder.exportSymbols("Juniper-SUBSCRIBER-MIB", juniSubscrLocalTable=juniSubscrLocalTable, juniSubscrLocalEntry=juniSubscrLocalEntry, PYSNMP_MODULE_ID=juniSubscriberMIB, juniSubscrLocal=juniSubscrLocal, juniSubscriberMIBCompliances=juniSubscriberMIBCompliances, juniSubscrLocalEncaps=juniSubscrLocalEncaps, juniSubscrLocalAuthentication=juniSubscrLocalAuthentication, juniSubscrLocalPassword=juniSubscrLocalPassword, juniSubscriberMIB=juniSubscriberMIB, juniSubscriberMIBConformance=juniSubscriberMIBConformance, juniSubscriberCompliance2=juniSubscriberCompliance2, juniSubscrLocalPasswordPrefix=juniSubscrLocalPasswordPrefix, juniSubscrLocalControl=juniSubscrLocalControl, juniSubscrLocalIfIndex=juniSubscrLocalIfIndex, juniSubscriberLocalGroup2=juniSubscriberLocalGroup2, juniSubscriberCompliance=juniSubscriberCompliance, juniSubscriberMIBGroups=juniSubscriberMIBGroups, juniSubscriberLocalGroup=juniSubscriberLocalGroup, juniSubscrLocalNamePrefix=juniSubscrLocalNamePrefix, juniSubscrLocalName=juniSubscrLocalName, JuniSubscrEncaps=JuniSubscrEncaps, juniSubscrObjects=juniSubscrObjects, juniSubscrLocalDomain=juniSubscrLocalDomain)
