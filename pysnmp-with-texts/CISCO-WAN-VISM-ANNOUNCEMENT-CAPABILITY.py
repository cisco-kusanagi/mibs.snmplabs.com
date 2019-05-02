#
# PySNMP MIB module CISCO-WAN-VISM-ANNOUNCEMENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-VISM-ANNOUNCEMENT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:20:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, NotificationType, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, IpAddress, Integer32, ModuleIdentity, Bits, Gauge32, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "IpAddress", "Integer32", "ModuleIdentity", "Bits", "Gauge32", "Counter32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cwAnnouncementCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 354))
cwAnnouncementCapability.setRevisions(('2001-10-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cwAnnouncementCapability.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: cwAnnouncementCapability.setLastUpdated('200112260000Z')
if mibBuilder.loadTexts: cwAnnouncementCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cwAnnouncementCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-vism@cisco.com')
if mibBuilder.loadTexts: cwAnnouncementCapability.setDescription('The Agent Capabilities for CISCO-WAN-ANNOUNCEMENT-MIB.')
cwAnnouncementCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 354, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAnnouncementCapabilityV3R00 = cwAnnouncementCapabilityV3R00.setProductRelease('VISM Release3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAnnouncementCapabilityV3R00 = cwAnnouncementCapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: cwAnnouncementCapabilityV3R00.setDescription('CISCO-WAN-ANNOUNCEMENT-MIB Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-ANNOUNCEMENT-CAPABILITY", cwAnnouncementCapability=cwAnnouncementCapability, PYSNMP_MODULE_ID=cwAnnouncementCapability, cwAnnouncementCapabilityV3R00=cwAnnouncementCapabilityV3R00)
