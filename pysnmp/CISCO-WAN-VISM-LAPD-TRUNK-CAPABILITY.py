#
# PySNMP MIB module CISCO-WAN-VISM-LAPD-TRUNK-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-VISM-LAPD-TRUNK-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:04:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
iso, MibIdentifier, Integer32, ObjectIdentity, Bits, Unsigned32, Gauge32, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "Integer32", "ObjectIdentity", "Bits", "Unsigned32", "Gauge32", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "TimeTicks", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cwVismLapdTrunkCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 336))
cwVismLapdTrunkCapability.setRevisions(('2001-03-15 00:00',))
if mibBuilder.loadTexts: cwVismLapdTrunkCapability.setLastUpdated('200108220000Z')
if mibBuilder.loadTexts: cwVismLapdTrunkCapability.setOrganization('Cisco Systems, Inc.')
cwVismLapdTrunkCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 336, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismLapdTrunkCapabilityV2R00 = cwVismLapdTrunkCapabilityV2R00.setProductRelease('VISM Release2.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismLapdTrunkCapabilityV2R00 = cwVismLapdTrunkCapabilityV2R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-VISM-LAPD-TRUNK-CAPABILITY", cwVismLapdTrunkCapabilityV2R00=cwVismLapdTrunkCapabilityV2R00, cwVismLapdTrunkCapability=cwVismLapdTrunkCapability, PYSNMP_MODULE_ID=cwVismLapdTrunkCapability)
