#
# PySNMP MIB module Unisphere-Data-SUBSCRIBER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-SUBSCRIBER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, MibIdentifier, IpAddress, Counter32, ObjectIdentity, Unsigned32, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Bits, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "IpAddress", "Counter32", "ObjectIdentity", "Unsigned32", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Bits", "TimeTicks", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdEnable, = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdEnable")
usdSubscriberMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49))
usdSubscriberMIB.setRevisions(('2002-05-10 19:53', '2000-11-16 00:00',))
if mibBuilder.loadTexts: usdSubscriberMIB.setLastUpdated('200205101953Z')
if mibBuilder.loadTexts: usdSubscriberMIB.setOrganization('Unisphere Networks, Inc.')
class UsdSubscrEncaps(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 19))
    namedValues = NamedValues(("ip", 0), ("bridgedEthernet", 19))

usdSubscrObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1))
usdSubscrLocal = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1))
usdSubscrLocalTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1), )
if mibBuilder.loadTexts: usdSubscrLocalTable.setStatus('current')
usdSubscrLocalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1), ).setIndexNames((0, "Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalIfIndex"), (0, "Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalEncaps"))
if mibBuilder.loadTexts: usdSubscrLocalEntry.setStatus('current')
usdSubscrLocalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: usdSubscrLocalIfIndex.setStatus('current')
usdSubscrLocalEncaps = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 2), UsdSubscrEncaps())
if mibBuilder.loadTexts: usdSubscrLocalEncaps.setStatus('current')
usdSubscrLocalControl = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ok", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSubscrLocalControl.setStatus('current')
usdSubscrLocalNamePrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 4), UsdEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSubscrLocalNamePrefix.setStatus('current')
usdSubscrLocalName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSubscrLocalName.setStatus('current')
usdSubscrLocalPasswordPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 6), UsdEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSubscrLocalPasswordPrefix.setStatus('current')
usdSubscrLocalPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSubscrLocalPassword.setStatus('current')
usdSubscrLocalDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSubscrLocalDomain.setStatus('current')
usdSubscrLocalAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 9), UsdEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSubscrLocalAuthentication.setStatus('current')
usdSubscriberMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4))
usdSubscriberMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 1))
usdSubscriberMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 2))
usdSubscriberCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 1, 1)).setObjects(("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscriberLocalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSubscriberCompliance = usdSubscriberCompliance.setStatus('obsolete')
usdSubscriberCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 1, 2)).setObjects(("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscriberLocalGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSubscriberCompliance2 = usdSubscriberCompliance2.setStatus('current')
usdSubscriberLocalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 2, 1)).setObjects(("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalControl"), ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalNamePrefix"), ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalName"), ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalPasswordPrefix"), ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalPassword"), ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalDomain"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSubscriberLocalGroup = usdSubscriberLocalGroup.setStatus('obsolete')
usdSubscriberLocalGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 2, 2)).setObjects(("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalControl"), ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalNamePrefix"), ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalName"), ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalPasswordPrefix"), ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalPassword"), ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalDomain"), ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalAuthentication"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSubscriberLocalGroup2 = usdSubscriberLocalGroup2.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-SUBSCRIBER-MIB", usdSubscrLocalIfIndex=usdSubscrLocalIfIndex, UsdSubscrEncaps=UsdSubscrEncaps, PYSNMP_MODULE_ID=usdSubscriberMIB, usdSubscrLocalEntry=usdSubscrLocalEntry, usdSubscriberMIBGroups=usdSubscriberMIBGroups, usdSubscrLocalDomain=usdSubscrLocalDomain, usdSubscrObjects=usdSubscrObjects, usdSubscrLocal=usdSubscrLocal, usdSubscrLocalName=usdSubscrLocalName, usdSubscriberCompliance2=usdSubscriberCompliance2, usdSubscriberCompliance=usdSubscriberCompliance, usdSubscriberLocalGroup2=usdSubscriberLocalGroup2, usdSubscriberLocalGroup=usdSubscriberLocalGroup, usdSubscrLocalPassword=usdSubscrLocalPassword, usdSubscriberMIBCompliances=usdSubscriberMIBCompliances, usdSubscrLocalPasswordPrefix=usdSubscrLocalPasswordPrefix, usdSubscrLocalTable=usdSubscrLocalTable, usdSubscrLocalAuthentication=usdSubscrLocalAuthentication, usdSubscrLocalNamePrefix=usdSubscrLocalNamePrefix, usdSubscrLocalControl=usdSubscrLocalControl, usdSubscrLocalEncaps=usdSubscrLocalEncaps, usdSubscriberMIB=usdSubscriberMIB, usdSubscriberMIBConformance=usdSubscriberMIBConformance)
