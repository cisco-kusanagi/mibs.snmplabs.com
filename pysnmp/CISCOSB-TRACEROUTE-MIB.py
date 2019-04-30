#
# PySNMP MIB module CISCOSB-TRACEROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-TRACEROUTE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:07:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, ObjectIdentity, Counter64, Integer32, NotificationType, TimeTicks, Bits, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "ObjectIdentity", "Counter64", "Integer32", "NotificationType", "TimeTicks", "Bits", "MibIdentifier", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlTraceRoute = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 81))
rlTraceRoute.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlTraceRoute.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlTraceRoute.setOrganization('Cisco Small Business')
rlTraceRouteMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 81, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTraceRouteMibVersion.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-TRACEROUTE-MIB", PYSNMP_MODULE_ID=rlTraceRoute, rlTraceRouteMibVersion=rlTraceRouteMibVersion, rlTraceRoute=rlTraceRoute)
