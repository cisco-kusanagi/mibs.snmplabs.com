#
# PySNMP MIB module ALCATEL-IND1-GLOBALROUTETABLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-GLOBALROUTETABLE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:02:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
routingIND1GlobalRouteTable, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "routingIND1GlobalRouteTable")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
IpAddress, MibIdentifier, Counter32, Bits, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, ObjectIdentity, ModuleIdentity, Integer32, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Counter32", "Bits", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Integer32", "NotificationType", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
alcatelIND1GRTMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1))
alcatelIND1GRTMIB.setRevisions(('2011-04-28 00:00',))
if mibBuilder.loadTexts: alcatelIND1GRTMIB.setLastUpdated('201212010000Z')
if mibBuilder.loadTexts: alcatelIND1GRTMIB.setOrganization('Alcatel-Lucent')
alcatelIND1GRTMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1))
alaGrtConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1))
class AlaGrtRouteDistinguisher(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

alaGrtRouteTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1), )
if mibBuilder.loadTexts: alaGrtRouteTable.setStatus('current')
alaGrtRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteDistinguisher"), (0, "ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteDest"), (0, "ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteMaskLen"), (0, "ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteNextHop"))
if mibBuilder.loadTexts: alaGrtRouteEntry.setStatus('current')
alaGrtRouteDistinguisher = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 1), AlaGrtRouteDistinguisher())
if mibBuilder.loadTexts: alaGrtRouteDistinguisher.setStatus('current')
alaGrtRouteDest = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 2), IpAddress())
if mibBuilder.loadTexts: alaGrtRouteDest.setStatus('current')
alaGrtRouteMaskLen = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 3), Unsigned32())
if mibBuilder.loadTexts: alaGrtRouteMaskLen.setStatus('current')
alaGrtRouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 4), IpAddress())
if mibBuilder.loadTexts: alaGrtRouteNextHop.setStatus('current')
alaGrtRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaGrtRouteMetric.setStatus('current')
alaGrtRouteTag = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaGrtRouteTag.setStatus('current')
alaGrtRouteVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaGrtRouteVrfName.setStatus('current')
alaGrtRouteIsid = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaGrtRouteIsid.setStatus('current')
alcatelIND1GRTMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 2))
alcatelIND1GRTMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 2, 1))
alcatelIND1GRTMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 2, 2))
alaGrtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaGrtCompliance = alaGrtCompliance.setStatus('current')
alaGrtConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteMetric"), ("ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteTag"), ("ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteVrfName"), ("ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteIsid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaGrtConfigMIBGroup = alaGrtConfigMIBGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-GLOBALROUTETABLE-MIB", PYSNMP_MODULE_ID=alcatelIND1GRTMIB, alaGrtRouteMaskLen=alaGrtRouteMaskLen, alaGrtRouteMetric=alaGrtRouteMetric, alaGrtRouteTable=alaGrtRouteTable, alaGrtRouteEntry=alaGrtRouteEntry, alcatelIND1GRTMIBCompliances=alcatelIND1GRTMIBCompliances, alcatelIND1GRTMIBGroups=alcatelIND1GRTMIBGroups, alcatelIND1GRTMIBObjects=alcatelIND1GRTMIBObjects, alaGrtRouteDistinguisher=alaGrtRouteDistinguisher, alaGrtRouteIsid=alaGrtRouteIsid, alaGrtRouteDest=alaGrtRouteDest, alaGrtCompliance=alaGrtCompliance, alaGrtConfigMIBGroup=alaGrtConfigMIBGroup, alcatelIND1GRTMIB=alcatelIND1GRTMIB, alaGrtRouteVrfName=alaGrtRouteVrfName, AlaGrtRouteDistinguisher=AlaGrtRouteDistinguisher, alaGrtConfig=alaGrtConfig, alcatelIND1GRTMIBConformance=alcatelIND1GRTMIBConformance, alaGrtRouteTag=alaGrtRouteTag, alaGrtRouteNextHop=alaGrtRouteNextHop)
