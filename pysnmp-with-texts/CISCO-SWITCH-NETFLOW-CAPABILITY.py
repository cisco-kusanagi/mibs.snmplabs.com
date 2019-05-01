#
# PySNMP MIB module CISCO-SWITCH-NETFLOW-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SWITCH-NETFLOW-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:13:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
Percent, = mibBuilder.importSymbols("CISCO-QOS-PIB-MIB", "Percent")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, Unsigned32, Counter32, MibIdentifier, Bits, ObjectIdentity, Integer32, IpAddress, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Unsigned32", "Counter32", "MibIdentifier", "Bits", "ObjectIdentity", "Integer32", "IpAddress", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSwitchNetflowCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 602))
ciscoSwitchNetflowCapability.setRevisions(('2012-09-11 00:00', '2010-11-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSwitchNetflowCapability.setRevisionsDescriptions(('Added apability statement csnCapV15R0101SYPCat6kPfc3.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSwitchNetflowCapability.setLastUpdated('201209110000Z')
if mibBuilder.loadTexts: ciscoSwitchNetflowCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSwitchNetflowCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSwitchNetflowCapability.setDescription('The capabilities description of CISCO-SWITCH-NETFLOW-MIB.')
csnCapV12R0250SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 602, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnCapV12R0250SYPCat6kPfc4 = csnCapV12R0250SYPCat6kPfc4.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnCapV12R0250SYPCat6kPfc4 = csnCapV12R0250SYPCat6kPfc4.setStatus('current')
if mibBuilder.loadTexts: csnCapV12R0250SYPCat6kPfc4.setDescription('CISCO-SWITCH-NETFLOW-MIB capabilities.')
csnCapV15R0101SYPCat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 602, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnCapV15R0101SYPCat6kPfc3 = csnCapV15R0101SYPCat6kPfc3.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnCapV15R0101SYPCat6kPfc3 = csnCapV15R0101SYPCat6kPfc3.setStatus('current')
if mibBuilder.loadTexts: csnCapV15R0101SYPCat6kPfc3.setDescription('CISCO-SWITCH-NETFLOW-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SWITCH-NETFLOW-CAPABILITY", PYSNMP_MODULE_ID=ciscoSwitchNetflowCapability, csnCapV15R0101SYPCat6kPfc3=csnCapV15R0101SYPCat6kPfc3, ciscoSwitchNetflowCapability=ciscoSwitchNetflowCapability, csnCapV12R0250SYPCat6kPfc4=csnCapV12R0250SYPCat6kPfc4)
