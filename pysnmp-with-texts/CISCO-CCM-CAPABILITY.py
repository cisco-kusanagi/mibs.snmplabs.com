#
# PySNMP MIB module CISCO-CCM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CCM-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:52:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Integer32, TimeTicks, ModuleIdentity, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Counter64, Counter32, NotificationType, Gauge32, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "ModuleIdentity", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Counter64", "Counter32", "NotificationType", "Gauge32", "Bits", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCCMCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 211))
ciscoCCMCapability.setRevisions(('2011-06-14 00:00', '2009-12-15 00:00', '2008-08-21 00:00', '2008-02-20 00:00', '2005-11-21 00:00', '2003-10-03 00:00', '2002-03-21 00:00', '2001-07-02 00:00', '2001-06-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCCMCapability.setRevisionsDescriptions(('Added the agent capabilities for Cisco Unified Call Manager version 8.5', "Added the agent capabilities for Cisco Unified Communications Manager (CUCM) 8.0 release. The SYNTAX classes for the objects(ccmPhFailedTblLastAddedIndex, ccmPhStatUpdtTblLastAddedIndex and ccmPhonePhysicalAddress) are removed as they don't give any additional info.", 'Added the agent capabilities for Cisco Unified Communications Manager (CUCM) 7.1 release', 'Added the agent capabilities for Cisco Unified Communications Manager (CUCM) 7.0 release', 'Added the agent capabilities for Cisco Call Manager 5.0 release.', 'Added the agent capabilities for Cisco Call Manager 4.0 release.', 'Added the agent capabilities for Cisco Call Manager 3.3 release.', 'Added the agent capabilities for Cisco Call Manager 3.0 release.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCCMCapability.setLastUpdated('201106140000Z')
if mibBuilder.loadTexts: ciscoCCMCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCCMCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-selsius@cisco.com')
if mibBuilder.loadTexts: ciscoCCMCapability.setDescription('Agent capabilities for CISCO-CCM-MIB')
ciscoCCMCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R00 = ciscoCCMCapabilityV3R00.setProductRelease('Cisco Call Manager 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R00 = ciscoCCMCapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoCCMCapabilityV3R00.setDescription('Cisco Call Manager Agent capabilities')
ciscoCCMCapabilityV3R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R01 = ciscoCCMCapabilityV3R01.setProductRelease('Cisco Call Manager 3.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R01 = ciscoCCMCapabilityV3R01.setStatus('current')
if mibBuilder.loadTexts: ciscoCCMCapabilityV3R01.setDescription('Cisco Call Manager Agent capabilities')
ciscoCCMCapabilityV3R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R03 = ciscoCCMCapabilityV3R03.setProductRelease('Cisco Call Manager 3.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R03 = ciscoCCMCapabilityV3R03.setStatus('obsolete')
if mibBuilder.loadTexts: ciscoCCMCapabilityV3R03.setDescription('Cisco Call Manager Agent capabilities')
ciscoCCMCapabilityV3R03Rev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R03Rev1 = ciscoCCMCapabilityV3R03Rev1.setProductRelease('Cisco Call Manager 3.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R03Rev1 = ciscoCCMCapabilityV3R03Rev1.setStatus('current')
if mibBuilder.loadTexts: ciscoCCMCapabilityV3R03Rev1.setDescription('Cisco Call Manager Agent capabilities')
ciscoCCMCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV4R00 = ciscoCCMCapabilityV4R00.setProductRelease('Cisco Call Manager 4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV4R00 = ciscoCCMCapabilityV4R00.setStatus('current')
if mibBuilder.loadTexts: ciscoCCMCapabilityV4R00.setDescription('Cisco Call Manager Agent capabilities')
ciscoCCMCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV5R00 = ciscoCCMCapabilityV5R00.setProductRelease('Cisco Call Manager 5.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV5R00 = ciscoCCMCapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: ciscoCCMCapabilityV5R00.setDescription('Cisco Call Manager Agent capabilities')
ciscoCCMCapabilityV7R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV7R00 = ciscoCCMCapabilityV7R00.setProductRelease('Cisco Unified Communications Manager 7.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV7R00 = ciscoCCMCapabilityV7R00.setStatus('current')
if mibBuilder.loadTexts: ciscoCCMCapabilityV7R00.setDescription('Cisco Unified Communications Manager Agent capabilities')
ciscoCCMCapabilityV7R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV7R01 = ciscoCCMCapabilityV7R01.setProductRelease('Cisco Unified Communications Manager 7.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV7R01 = ciscoCCMCapabilityV7R01.setStatus('current')
if mibBuilder.loadTexts: ciscoCCMCapabilityV7R01.setDescription('Cisco Unified Communications Manager Agent capabilities')
ciscoCCMCapabilityV8R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV8R00 = ciscoCCMCapabilityV8R00.setProductRelease('Cisco Unified Communications Manager 8.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV8R00 = ciscoCCMCapabilityV8R00.setStatus('current')
if mibBuilder.loadTexts: ciscoCCMCapabilityV8R00.setDescription('Cisco Unified Communications Manager Agent capabilities')
ciscoCCMCapabilityV8R05 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV8R05 = ciscoCCMCapabilityV8R05.setProductRelease('Cisco Unified Communications Manager 8.5')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV8R05 = ciscoCCMCapabilityV8R05.setStatus('current')
if mibBuilder.loadTexts: ciscoCCMCapabilityV8R05.setDescription('Cisco Unified Communications Manager Agent capabilities')
mibBuilder.exportSymbols("CISCO-CCM-CAPABILITY", ciscoCCMCapabilityV4R00=ciscoCCMCapabilityV4R00, ciscoCCMCapabilityV8R00=ciscoCCMCapabilityV8R00, ciscoCCMCapabilityV8R05=ciscoCCMCapabilityV8R05, ciscoCCMCapabilityV3R00=ciscoCCMCapabilityV3R00, ciscoCCMCapabilityV5R00=ciscoCCMCapabilityV5R00, ciscoCCMCapabilityV3R03=ciscoCCMCapabilityV3R03, ciscoCCMCapabilityV7R00=ciscoCCMCapabilityV7R00, PYSNMP_MODULE_ID=ciscoCCMCapability, ciscoCCMCapabilityV7R01=ciscoCCMCapabilityV7R01, ciscoCCMCapabilityV3R03Rev1=ciscoCCMCapabilityV3R03Rev1, ciscoCCMCapabilityV3R01=ciscoCCMCapabilityV3R01, ciscoCCMCapability=ciscoCCMCapability)
