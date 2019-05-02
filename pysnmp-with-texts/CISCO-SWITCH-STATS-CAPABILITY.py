#
# PySNMP MIB module CISCO-SWITCH-STATS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SWITCH-STATS-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:13:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
MibIdentifier, IpAddress, ModuleIdentity, Bits, ObjectIdentity, Unsigned32, Counter32, Counter64, Integer32, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "ModuleIdentity", "Bits", "ObjectIdentity", "Unsigned32", "Counter32", "Counter64", "Integer32", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSwitchStatsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 600))
ciscoSwitchStatsCapability.setRevisions(('2013-09-25 00:00', '2013-07-26 00:00', '2010-11-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSwitchStatsCapability.setRevisionsDescriptions(('Added capability statement csstCapV15R0102SYPCat6kPfc4 and csstCapV15R0102SYPCat6kPfc3.', 'Add agent capability statement csstCapNxOSV06R0104PN7k and csstCapNxOSV06R0201PMds.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSwitchStatsCapability.setLastUpdated('201309250000Z')
if mibBuilder.loadTexts: ciscoSwitchStatsCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSwitchStatsCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSwitchStatsCapability.setDescription('The capabilities description of CISCO-SWITCH-STATS-MIB.')
csstCapV12R0250SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 600, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV12R0250SYPCat6kPfc4 = csstCapV12R0250SYPCat6kPfc4.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV12R0250SYPCat6kPfc4 = csstCapV12R0250SYPCat6kPfc4.setStatus('current')
if mibBuilder.loadTexts: csstCapV12R0250SYPCat6kPfc4.setDescription('CISCO-SWITCH-STATS-MIB capabilities.')
csstCapNxOSV06R0104PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 600, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapNxOSV06R0104PN7k = csstCapNxOSV06R0104PN7k.setProductRelease('Cisco NX-OS 6.1(4) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapNxOSV06R0104PN7k = csstCapNxOSV06R0104PN7k.setStatus('current')
if mibBuilder.loadTexts: csstCapNxOSV06R0104PN7k.setDescription('CISCO-SWITCH-STATS-MIB capabilities.')
csstCapNxOSV06R0201PMds = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 600, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapNxOSV06R0201PMds = csstCapNxOSV06R0201PMds.setProductRelease('Cisco NX-OS 6.2(1) on MDS series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapNxOSV06R0201PMds = csstCapNxOSV06R0201PMds.setStatus('current')
if mibBuilder.loadTexts: csstCapNxOSV06R0201PMds.setDescription('CISCO-SWITCH-STATS-MIB capabilities.')
csstCapV15R0102SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 600, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV15R0102SYPCat6kPfc4 = csstCapV15R0102SYPCat6kPfc4.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV15R0102SYPCat6kPfc4 = csstCapV15R0102SYPCat6kPfc4.setStatus('current')
if mibBuilder.loadTexts: csstCapV15R0102SYPCat6kPfc4.setDescription('CISCO-SWITCH-STATS-MIB capabilities.')
csstCapV15R0102SYPCat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 600, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV15R0102SYPCat6kPfc3 = csstCapV15R0102SYPCat6kPfc3.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                    series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV15R0102SYPCat6kPfc3 = csstCapV15R0102SYPCat6kPfc3.setStatus('current')
if mibBuilder.loadTexts: csstCapV15R0102SYPCat6kPfc3.setDescription('CISCO-SWITCH-STATS-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SWITCH-STATS-CAPABILITY", csstCapNxOSV06R0104PN7k=csstCapNxOSV06R0104PN7k, csstCapNxOSV06R0201PMds=csstCapNxOSV06R0201PMds, csstCapV12R0250SYPCat6kPfc4=csstCapV12R0250SYPCat6kPfc4, PYSNMP_MODULE_ID=ciscoSwitchStatsCapability, csstCapV15R0102SYPCat6kPfc4=csstCapV15R0102SYPCat6kPfc4, csstCapV15R0102SYPCat6kPfc3=csstCapV15R0102SYPCat6kPfc3, ciscoSwitchStatsCapability=ciscoSwitchStatsCapability)
