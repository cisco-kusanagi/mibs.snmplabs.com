#
# PySNMP MIB module CISCO-DIAMETER-CC-APPL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DIAMETER-CC-APPL-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:54:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, Gauge32, ObjectIdentity, IpAddress, Unsigned32, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, TimeTicks, MibIdentifier, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "ObjectIdentity", "IpAddress", "Unsigned32", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "TimeTicks", "MibIdentifier", "Integer32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoDiameterCCACapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 516))
ciscoDiameterCCACapability.setRevisions(('2006-09-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDiameterCCACapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDiameterCCACapability.setLastUpdated('200609060000Z')
if mibBuilder.loadTexts: ciscoDiameterCCACapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDiameterCCACapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-aaa@cisco.com')
if mibBuilder.loadTexts: ciscoDiameterCCACapability.setDescription('The capabilities description of CISCO-DIAMETER-CC-AAPL-MIB.')
ciscoDiameterCCACapabilityV12R0409XG = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 516, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDiameterCCACapabilityV12R0409XG = ciscoDiameterCCACapabilityV12R0409XG.setProductRelease('Cisco IOS 12.4(9)XG.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDiameterCCACapabilityV12R0409XG = ciscoDiameterCCACapabilityV12R0409XG.setStatus('current')
if mibBuilder.loadTexts: ciscoDiameterCCACapabilityV12R0409XG.setDescription('Cisco Diameter Credit Control Application MIB capabilities')
mibBuilder.exportSymbols("CISCO-DIAMETER-CC-APPL-CAPABILITY", ciscoDiameterCCACapabilityV12R0409XG=ciscoDiameterCCACapabilityV12R0409XG, ciscoDiameterCCACapability=ciscoDiameterCCACapability, PYSNMP_MODULE_ID=ciscoDiameterCCACapability)
