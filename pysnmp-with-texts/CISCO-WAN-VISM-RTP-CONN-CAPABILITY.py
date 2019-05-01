#
# PySNMP MIB module CISCO-WAN-VISM-RTP-CONN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-VISM-RTP-CONN-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:21:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Bits, TimeTicks, iso, Counter32, Unsigned32, Gauge32, ModuleIdentity, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "iso", "Counter32", "Unsigned32", "Gauge32", "ModuleIdentity", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Integer32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cwVismRtpConnCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 337))
cwVismRtpConnCapability.setRevisions(('2001-03-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cwVismRtpConnCapability.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: cwVismRtpConnCapability.setLastUpdated('200108220000Z')
if mibBuilder.loadTexts: cwVismRtpConnCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cwVismRtpConnCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-vism@cisco.com')
if mibBuilder.loadTexts: cwVismRtpConnCapability.setDescription('The Agent Capabilities for CISCO-WAN-RTP-CONN-MIB.')
cwVismRtpConnCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 337, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismRtpConnCapabilityV2R00 = cwVismRtpConnCapabilityV2R00.setProductRelease('VISM Release2.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismRtpConnCapabilityV2R00 = cwVismRtpConnCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: cwVismRtpConnCapabilityV2R00.setDescription('CISCO-WAN-RTP-CONN-MIB Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-RTP-CONN-CAPABILITY", PYSNMP_MODULE_ID=cwVismRtpConnCapability, cwVismRtpConnCapability=cwVismRtpConnCapability, cwVismRtpConnCapabilityV2R00=cwVismRtpConnCapabilityV2R00)
