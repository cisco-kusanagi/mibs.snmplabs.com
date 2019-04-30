#
# PySNMP MIB module Unisphere-Data-AUTOCONFIGURE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-AUTOCONFIGURE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Unsigned32, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Counter32, NotificationType, TimeTicks, Gauge32, ModuleIdentity, ObjectIdentity, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Counter32", "NotificationType", "TimeTicks", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdEnable, = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdEnable")
usdAutoConfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48))
usdAutoConfMIB.setRevisions(('2002-11-18 00:00', '2000-11-16 00:00',))
if mibBuilder.loadTexts: usdAutoConfMIB.setLastUpdated('200211190000Z')
if mibBuilder.loadTexts: usdAutoConfMIB.setOrganization('Unisphere Networks Inc.')
class UsdAutoConfEncaps(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 17, 19))
    namedValues = NamedValues(("ip", 0), ("ppp", 1), ("pppoe", 17), ("bridgedEthernet", 19))

usdAutoConfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1))
usdAutoConf = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1))
usdAutoConfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1), )
if mibBuilder.loadTexts: usdAutoConfTable.setStatus('current')
usdAutoConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1), ).setIndexNames((0, "Unisphere-Data-AUTOCONFIGURE-MIB", "usdAutoConfIfIndex"), (0, "Unisphere-Data-AUTOCONFIGURE-MIB", "usdAutoConfEncaps"))
if mibBuilder.loadTexts: usdAutoConfEntry.setStatus('current')
usdAutoConfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: usdAutoConfIfIndex.setStatus('current')
usdAutoConfEncaps = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 2), UsdAutoConfEncaps())
if mibBuilder.loadTexts: usdAutoConfEncaps.setStatus('current')
usdAutoConfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 3), UsdEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdAutoConfEnable.setStatus('current')
usdAutoConfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4))
usdAutoConfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 1))
usdAutoConfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 2))
usdAutoConfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 1, 1)).setObjects(("Unisphere-Data-AUTOCONFIGURE-MIB", "usdAutoConfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAutoConfCompliance = usdAutoConfCompliance.setStatus('current')
usdAutoConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 2, 1)).setObjects(("Unisphere-Data-AUTOCONFIGURE-MIB", "usdAutoConfEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAutoConfGroup = usdAutoConfGroup.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-AUTOCONFIGURE-MIB", usdAutoConfIfIndex=usdAutoConfIfIndex, usdAutoConfGroup=usdAutoConfGroup, usdAutoConfMIBConformance=usdAutoConfMIBConformance, usdAutoConfMIB=usdAutoConfMIB, usdAutoConfCompliance=usdAutoConfCompliance, UsdAutoConfEncaps=UsdAutoConfEncaps, usdAutoConfEncaps=usdAutoConfEncaps, usdAutoConfTable=usdAutoConfTable, usdAutoConfEntry=usdAutoConfEntry, usdAutoConfMIBCompliances=usdAutoConfMIBCompliances, usdAutoConf=usdAutoConf, usdAutoConfObjects=usdAutoConfObjects, usdAutoConfEnable=usdAutoConfEnable, usdAutoConfMIBGroups=usdAutoConfMIBGroups, PYSNMP_MODULE_ID=usdAutoConfMIB)
