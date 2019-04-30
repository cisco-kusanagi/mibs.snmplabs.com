#
# PySNMP MIB module CISCO-WAN-CELL-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-CELL-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:04:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Unsigned32, IpAddress, iso, Gauge32, ModuleIdentity, TimeTicks, Bits, Integer32, ObjectIdentity, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "iso", "Gauge32", "ModuleIdentity", "TimeTicks", "Bits", "Integer32", "ObjectIdentity", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanCellExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 625))
ciscoWanCellExtCapability.setRevisions(('2014-03-21 00:00',))
if mibBuilder.loadTexts: ciscoWanCellExtCapability.setLastUpdated('201403210000Z')
if mibBuilder.loadTexts: ciscoWanCellExtCapability.setOrganization('Cisco Systems, Inc.')
cwceCapV15R0501PIsr = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 625, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwceCapV15R0501PIsr = cwceCapV15R0501PIsr.setProductRelease('Cisco IOS 15.5(1) Version on Cisco ISR\n                    3900/2900/1900/3800/2800/1800/800 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwceCapV15R0501PIsr = cwceCapV15R0501PIsr.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-CELL-EXT-CAPABILITY", ciscoWanCellExtCapability=ciscoWanCellExtCapability, PYSNMP_MODULE_ID=ciscoWanCellExtCapability, cwceCapV15R0501PIsr=cwceCapV15R0501PIsr)
