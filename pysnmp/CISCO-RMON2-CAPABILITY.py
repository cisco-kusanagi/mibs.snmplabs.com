#
# PySNMP MIB module CISCO-RMON2-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RMON2-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:54:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
TimeTicks, NotificationType, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, Gauge32, Counter32, MibIdentifier, Unsigned32, Counter64, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "Gauge32", "Counter32", "MibIdentifier", "Unsigned32", "Counter64", "iso", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRmon2Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 361))
ciscoRmon2Capability.setRevisions(('2003-10-01 00:00',))
if mibBuilder.loadTexts: ciscoRmon2Capability.setLastUpdated('200310010000Z')
if mibBuilder.loadTexts: ciscoRmon2Capability.setOrganization('Cisco Systems, Inc.')
ciscoRmon2CapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 361, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmon2CapCatOSV08R0101 = ciscoRmon2CapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmon2CapCatOSV08R0101 = ciscoRmon2CapCatOSV08R0101.setStatus('current')
mibBuilder.exportSymbols("CISCO-RMON2-CAPABILITY", ciscoRmon2Capability=ciscoRmon2Capability, PYSNMP_MODULE_ID=ciscoRmon2Capability, ciscoRmon2CapCatOSV08R0101=ciscoRmon2CapCatOSV08R0101)
