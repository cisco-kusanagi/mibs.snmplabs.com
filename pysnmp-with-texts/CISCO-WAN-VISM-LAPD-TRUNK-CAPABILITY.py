#
# PySNMP MIB module CISCO-WAN-VISM-LAPD-TRUNK-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-VISM-LAPD-TRUNK-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:21:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Unsigned32, NotificationType, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, Bits, ObjectIdentity, IpAddress, ModuleIdentity, iso, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "Bits", "ObjectIdentity", "IpAddress", "ModuleIdentity", "iso", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cwVismLapdTrunkCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 336))
cwVismLapdTrunkCapability.setRevisions(('2001-03-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cwVismLapdTrunkCapability.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: cwVismLapdTrunkCapability.setLastUpdated('200108220000Z')
if mibBuilder.loadTexts: cwVismLapdTrunkCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cwVismLapdTrunkCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-vism@cisco.com')
if mibBuilder.loadTexts: cwVismLapdTrunkCapability.setDescription('The Agent Capabilities for CISCO-WAN-LAPD-TRUNK-MIB.')
cwVismLapdTrunkCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 336, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismLapdTrunkCapabilityV2R00 = cwVismLapdTrunkCapabilityV2R00.setProductRelease('VISM Release2.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismLapdTrunkCapabilityV2R00 = cwVismLapdTrunkCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: cwVismLapdTrunkCapabilityV2R00.setDescription('CISCO-WAN-LAPD-TRUNK-MIB Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-LAPD-TRUNK-CAPABILITY", cwVismLapdTrunkCapability=cwVismLapdTrunkCapability, PYSNMP_MODULE_ID=cwVismLapdTrunkCapability, cwVismLapdTrunkCapabilityV2R00=cwVismLapdTrunkCapabilityV2R00)
