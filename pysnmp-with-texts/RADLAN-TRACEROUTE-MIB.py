#
# PySNMP MIB module RADLAN-TRACEROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-TRACEROUTE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:49:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, MibIdentifier, iso, Integer32, Bits, NotificationType, IpAddress, ModuleIdentity, Counter32, TimeTicks, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "MibIdentifier", "iso", "Integer32", "Bits", "NotificationType", "IpAddress", "ModuleIdentity", "Counter32", "TimeTicks", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlTraceRoute = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 81))
rlTraceRoute.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlTraceRoute.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlTraceRoute.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlTraceRoute.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
if mibBuilder.loadTexts: rlTraceRoute.setContactInfo('www.marvell.com')
if mibBuilder.loadTexts: rlTraceRoute.setDescription('This private MIB module defines TRACE ROUTE private MIBs.')
rlTraceRouteMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 81, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTraceRouteMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlTraceRouteMibVersion.setDescription("MIB's version, the current version is 1.")
mibBuilder.exportSymbols("RADLAN-TRACEROUTE-MIB", PYSNMP_MODULE_ID=rlTraceRoute, rlTraceRoute=rlTraceRoute, rlTraceRouteMibVersion=rlTraceRouteMibVersion)
