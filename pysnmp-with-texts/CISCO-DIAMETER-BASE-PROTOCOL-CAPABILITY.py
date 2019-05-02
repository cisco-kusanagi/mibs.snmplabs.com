#
# PySNMP MIB module CISCO-DIAMETER-BASE-PROTOCOL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DIAMETER-BASE-PROTOCOL-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:54:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
MibIdentifier, Counter32, Integer32, iso, NotificationType, TimeTicks, ObjectIdentity, IpAddress, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "Integer32", "iso", "NotificationType", "TimeTicks", "ObjectIdentity", "IpAddress", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDiameterBasePCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 517))
ciscoDiameterBasePCapability.setRevisions(('2006-09-06 11:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDiameterBasePCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDiameterBasePCapability.setLastUpdated('200609061130Z')
if mibBuilder.loadTexts: ciscoDiameterBasePCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDiameterBasePCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-aaa@cisco.com')
if mibBuilder.loadTexts: ciscoDiameterBasePCapability.setDescription('The capabilities description of CISCO-DIAMETER-BASE-PROTOCOL-MIB.')
ciscoDiameterBasePCapabilityV12R0409XG = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 517, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDiameterBasePCapabilityV12R0409XG = ciscoDiameterBasePCapabilityV12R0409XG.setProductRelease('Cisco IOS 12.4(9)XG.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDiameterBasePCapabilityV12R0409XG = ciscoDiameterBasePCapabilityV12R0409XG.setStatus('current')
if mibBuilder.loadTexts: ciscoDiameterBasePCapabilityV12R0409XG.setDescription('Cisco Diameter Base Protocol MIB capabilities')
mibBuilder.exportSymbols("CISCO-DIAMETER-BASE-PROTOCOL-CAPABILITY", ciscoDiameterBasePCapabilityV12R0409XG=ciscoDiameterBasePCapabilityV12R0409XG, ciscoDiameterBasePCapability=ciscoDiameterBasePCapability, PYSNMP_MODULE_ID=ciscoDiameterBasePCapability)
