#
# PySNMP MIB module CISCO-DIAMETER-SG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DIAMETER-SG-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:54:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
IpAddress, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, Counter64, Unsigned32, Gauge32, NotificationType, MibIdentifier, iso, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "NotificationType", "MibIdentifier", "iso", "Bits", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDiameterSGCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 518))
ciscoDiameterSGCapability.setRevisions(('2006-09-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDiameterSGCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDiameterSGCapability.setLastUpdated('200609070000Z')
if mibBuilder.loadTexts: ciscoDiameterSGCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDiameterSGCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-aaa@cisco.com')
if mibBuilder.loadTexts: ciscoDiameterSGCapability.setDescription('The capabilities description of CISCO-DIAMETER-SG-MIB.')
ciscoDiameterSGCapabilityV12R0409XG = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 518, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDiameterSGCapabilityV12R0409XG = ciscoDiameterSGCapabilityV12R0409XG.setProductRelease('Cisco IOS 12.4(9)XG.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDiameterSGCapabilityV12R0409XG = ciscoDiameterSGCapabilityV12R0409XG.setStatus('current')
if mibBuilder.loadTexts: ciscoDiameterSGCapabilityV12R0409XG.setDescription('Cisco Diameter Server Group MIB capabilities')
mibBuilder.exportSymbols("CISCO-DIAMETER-SG-CAPABILITY", PYSNMP_MODULE_ID=ciscoDiameterSGCapability, ciscoDiameterSGCapability=ciscoDiameterSGCapability, ciscoDiameterSGCapabilityV12R0409XG=ciscoDiameterSGCapabilityV12R0409XG)
