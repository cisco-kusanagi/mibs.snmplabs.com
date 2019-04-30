#
# PySNMP MIB module CISCO-DIAMETER-BASE-PROTOCOL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DIAMETER-BASE-PROTOCOL-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:36:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Counter32, MibIdentifier, TimeTicks, ModuleIdentity, NotificationType, Counter64, Gauge32, IpAddress, iso, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "TimeTicks", "ModuleIdentity", "NotificationType", "Counter64", "Gauge32", "IpAddress", "iso", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDiameterBasePCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 517))
ciscoDiameterBasePCapability.setRevisions(('2006-09-06 11:30',))
if mibBuilder.loadTexts: ciscoDiameterBasePCapability.setLastUpdated('200609061130Z')
if mibBuilder.loadTexts: ciscoDiameterBasePCapability.setOrganization('Cisco Systems, Inc.')
ciscoDiameterBasePCapabilityV12R0409XG = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 517, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDiameterBasePCapabilityV12R0409XG = ciscoDiameterBasePCapabilityV12R0409XG.setProductRelease('Cisco IOS 12.4(9)XG.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDiameterBasePCapabilityV12R0409XG = ciscoDiameterBasePCapabilityV12R0409XG.setStatus('current')
mibBuilder.exportSymbols("CISCO-DIAMETER-BASE-PROTOCOL-CAPABILITY", ciscoDiameterBasePCapabilityV12R0409XG=ciscoDiameterBasePCapabilityV12R0409XG, ciscoDiameterBasePCapability=ciscoDiameterBasePCapability, PYSNMP_MODULE_ID=ciscoDiameterBasePCapability)
