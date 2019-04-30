#
# PySNMP MIB module NNCEXTVPTTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NNCEXTVPTTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:13:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
atmVclVpi, = mibBuilder.importSymbols("ATM-MIB", "atmVclVpi")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
nncExtensions, = mibBuilder.importSymbols("NNCGNI0001-SMI", "nncExtensions")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter64, IpAddress, iso, Counter32, Gauge32, MibIdentifier, Unsigned32, ObjectIdentity, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "iso", "Counter32", "Gauge32", "MibIdentifier", "Unsigned32", "ObjectIdentity", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nncExtVpttp = ModuleIdentity((1, 3, 6, 1, 4, 1, 123, 3, 80))
if mibBuilder.loadTexts: nncExtVpttp.setLastUpdated('200007211126Z')
if mibBuilder.loadTexts: nncExtVpttp.setOrganization('Alcatel Networks Corporation')
nncExtVpttpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 80, 1))
nncExtVpttpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 80, 3))
nncExtVpttpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 80, 4))
nncCrVpTrailTerminationPointTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 80, 1, 1), )
if mibBuilder.loadTexts: nncCrVpTrailTerminationPointTable.setStatus('current')
nncCrVpTrailTerminationPointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 80, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"))
if mibBuilder.loadTexts: nncCrVpTrailTerminationPointEntry.setStatus('current')
nncCrVpTrailTerminationPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 80, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disabled", 0), ("enabledWithNoAlarms", 1), ("enabledWithAlarms", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncCrVpTrailTerminationPoint.setStatus('current')
nncCrVpTrailTerminationPointGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 123, 3, 80, 3, 1)).setObjects(("NNCEXTVPTTP-MIB", "nncCrVpTrailTerminationPoint"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nncCrVpTrailTerminationPointGroup = nncCrVpTrailTerminationPointGroup.setStatus('current')
nncVpttpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 123, 3, 80, 4, 1)).setObjects(("NNCEXTVPTTP-MIB", "nncCrVpTrailTerminationPointGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nncVpttpCompliance = nncVpttpCompliance.setStatus('current')
mibBuilder.exportSymbols("NNCEXTVPTTP-MIB", nncExtVpttpObjects=nncExtVpttpObjects, nncCrVpTrailTerminationPointTable=nncCrVpTrailTerminationPointTable, nncExtVpttpGroups=nncExtVpttpGroups, PYSNMP_MODULE_ID=nncExtVpttp, nncVpttpCompliance=nncVpttpCompliance, nncCrVpTrailTerminationPointGroup=nncCrVpTrailTerminationPointGroup, nncExtVpttp=nncExtVpttp, nncCrVpTrailTerminationPointEntry=nncCrVpTrailTerminationPointEntry, nncCrVpTrailTerminationPoint=nncCrVpTrailTerminationPoint, nncExtVpttpCompliances=nncExtVpttpCompliances)
