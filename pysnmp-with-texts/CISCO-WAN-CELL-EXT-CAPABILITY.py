#
# PySNMP MIB module CISCO-WAN-CELL-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-CELL-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:20:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, Counter32, Unsigned32, Gauge32, MibIdentifier, iso, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "Counter32", "Unsigned32", "Gauge32", "MibIdentifier", "iso", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWanCellExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 625))
ciscoWanCellExtCapability.setRevisions(('2014-03-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanCellExtCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoWanCellExtCapability.setLastUpdated('201403210000Z')
if mibBuilder.loadTexts: ciscoWanCellExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanCellExtCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoWanCellExtCapability.setDescription('The capabilities description of CISCO-WAN-CELL-EXT-MIB.')
cwceCapV15R0501PIsr = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 625, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwceCapV15R0501PIsr = cwceCapV15R0501PIsr.setProductRelease('Cisco IOS 15.5(1) Version on Cisco ISR\n                    3900/2900/1900/3800/2800/1800/800 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwceCapV15R0501PIsr = cwceCapV15R0501PIsr.setStatus('current')
if mibBuilder.loadTexts: cwceCapV15R0501PIsr.setDescription('CISCO-WAN-CELL-EXT-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-WAN-CELL-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoWanCellExtCapability, cwceCapV15R0501PIsr=cwceCapV15R0501PIsr, ciscoWanCellExtCapability=ciscoWanCellExtCapability)
