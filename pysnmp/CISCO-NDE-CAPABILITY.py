#
# PySNMP MIB module CISCO-NDE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-NDE-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:51:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, Gauge32, TimeTicks, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, NotificationType, IpAddress, Bits, Integer32, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "TimeTicks", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "NotificationType", "IpAddress", "Bits", "Integer32", "iso", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoNdeCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 328))
ciscoNdeCapability.setRevisions(('2010-11-04 00:00', '2004-01-27 00:00', '2003-08-26 00:00',))
if mibBuilder.loadTexts: ciscoNdeCapability.setLastUpdated('201011040000Z')
if mibBuilder.loadTexts: ciscoNdeCapability.setOrganization('Cisco Systems, Inc.')
ciscoNdeCapabilityV12R0119E = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 328, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNdeCapabilityV12R0119E = ciscoNdeCapabilityV12R0119E.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500 \n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNdeCapabilityV12R0119E = ciscoNdeCapabilityV12R0119E.setStatus('current')
ciscoNdeCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 328, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNdeCapCatOSV08R0301 = ciscoNdeCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500 \n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNdeCapCatOSV08R0301 = ciscoNdeCapCatOSV08R0301.setStatus('current')
ciscoNdeCapV12R0250SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 328, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNdeCapV12R0250SYPCat6kPfc4 = ciscoNdeCapV12R0250SYPCat6kPfc4.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500 \n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNdeCapV12R0250SYPCat6kPfc4 = ciscoNdeCapV12R0250SYPCat6kPfc4.setStatus('current')
mibBuilder.exportSymbols("CISCO-NDE-CAPABILITY", ciscoNdeCapCatOSV08R0301=ciscoNdeCapCatOSV08R0301, ciscoNdeCapability=ciscoNdeCapability, PYSNMP_MODULE_ID=ciscoNdeCapability, ciscoNdeCapabilityV12R0119E=ciscoNdeCapabilityV12R0119E, ciscoNdeCapV12R0250SYPCat6kPfc4=ciscoNdeCapV12R0250SYPCat6kPfc4)
