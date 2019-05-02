#
# PySNMP MIB module CISCO-SCTP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SCTP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:11:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Integer32, IpAddress, MibIdentifier, TimeTicks, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, Unsigned32, Counter64, Bits, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "MibIdentifier", "TimeTicks", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "Unsigned32", "Counter64", "Bits", "NotificationType", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ceSctpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 190))
ceSctpCapability.setRevisions(('2001-06-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ceSctpCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ceSctpCapability.setLastUpdated('200106050000Z')
if mibBuilder.loadTexts: ceSctpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ceSctpCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: tac@cisco.com')
if mibBuilder.loadTexts: ceSctpCapability.setDescription('Agent capabilities for the CISCO-SCTP-MIB.')
ceSctpCapabilityV12R021MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 190, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceSctpCapabilityV12R021MB1 = ceSctpCapabilityV12R021MB1.setProductRelease('Cisco IOS 12.2(1)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceSctpCapabilityV12R021MB1 = ceSctpCapabilityV12R021MB1.setStatus('current')
if mibBuilder.loadTexts: ceSctpCapabilityV12R021MB1.setDescription('IOS 12.2(1)MB1 Cisco CISCO-SCTP-MIB.my User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SCTP-CAPABILITY", ceSctpCapabilityV12R021MB1=ceSctpCapabilityV12R021MB1, ceSctpCapability=ceSctpCapability, PYSNMP_MODULE_ID=ceSctpCapability)
