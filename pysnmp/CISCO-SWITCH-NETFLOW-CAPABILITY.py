#
# PySNMP MIB module CISCO-SWITCH-NETFLOW-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SWITCH-NETFLOW-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:56:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
Percent, = mibBuilder.importSymbols("CISCO-QOS-PIB-MIB", "Percent")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
iso, IpAddress, Counter32, Integer32, NotificationType, Counter64, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, Bits, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "Counter32", "Integer32", "NotificationType", "Counter64", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "Bits", "MibIdentifier", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSwitchNetflowCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 602))
ciscoSwitchNetflowCapability.setRevisions(('2012-09-11 00:00', '2010-11-17 00:00',))
if mibBuilder.loadTexts: ciscoSwitchNetflowCapability.setLastUpdated('201209110000Z')
if mibBuilder.loadTexts: ciscoSwitchNetflowCapability.setOrganization('Cisco Systems, Inc.')
csnCapV12R0250SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 602, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnCapV12R0250SYPCat6kPfc4 = csnCapV12R0250SYPCat6kPfc4.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnCapV12R0250SYPCat6kPfc4 = csnCapV12R0250SYPCat6kPfc4.setStatus('current')
csnCapV15R0101SYPCat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 602, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnCapV15R0101SYPCat6kPfc3 = csnCapV15R0101SYPCat6kPfc3.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnCapV15R0101SYPCat6kPfc3 = csnCapV15R0101SYPCat6kPfc3.setStatus('current')
mibBuilder.exportSymbols("CISCO-SWITCH-NETFLOW-CAPABILITY", PYSNMP_MODULE_ID=ciscoSwitchNetflowCapability, ciscoSwitchNetflowCapability=ciscoSwitchNetflowCapability, csnCapV12R0250SYPCat6kPfc4=csnCapV12R0250SYPCat6kPfc4, csnCapV15R0101SYPCat6kPfc3=csnCapV15R0101SYPCat6kPfc3)
