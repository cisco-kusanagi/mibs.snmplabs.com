#
# PySNMP MIB module CISCO-AAA-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-AAA-CLIENT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:32:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
ModuleIdentity, TimeTicks, Counter32, iso, MibIdentifier, Integer32, Counter64, Unsigned32, IpAddress, ObjectIdentity, Gauge32, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Counter32", "iso", "MibIdentifier", "Integer32", "Counter64", "Unsigned32", "IpAddress", "ObjectIdentity", "Gauge32", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoAaaClientCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 322))
ciscoAaaClientCapability.setRevisions(('2004-02-03 00:00', '2003-08-06 00:00',))
if mibBuilder.loadTexts: ciscoAaaClientCapability.setLastUpdated('200402030000Z')
if mibBuilder.loadTexts: ciscoAaaClientCapability.setOrganization('Cisco Systems, Inc.')
ciscoAaaClientCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 322, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAaaClientCapCatOSV08R0101 = ciscoAaaClientCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAaaClientCapCatOSV08R0101 = ciscoAaaClientCapCatOSV08R0101.setStatus('current')
mibBuilder.exportSymbols("CISCO-AAA-CLIENT-CAPABILITY", ciscoAaaClientCapability=ciscoAaaClientCapability, ciscoAaaClientCapCatOSV08R0101=ciscoAaaClientCapCatOSV08R0101, PYSNMP_MODULE_ID=ciscoAaaClientCapability)
