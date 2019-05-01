#
# PySNMP MIB module CISCO-ENHANCED-SLB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENHANCED-SLB-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:56:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
iso, IpAddress, Unsigned32, Integer32, Bits, Gauge32, ObjectIdentity, TimeTicks, Counter32, Counter64, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "Unsigned32", "Integer32", "Bits", "Gauge32", "ObjectIdentity", "TimeTicks", "Counter32", "Counter64", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEnhancedSlbCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 507))
ciscoEnhancedSlbCapability.setRevisions(('2008-07-07 00:00', '2008-02-08 00:00', '2006-05-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEnhancedSlbCapability.setRevisionsDescriptions(('Added capability statement ciscoEnhancedSlbCapc4710aceVA3R10 for ACE 4710 Application Control Engine Appliance.', 'Added capability statement ciscoEnhancedSlbCapc4710aceVA1R70 for ACE 4710 Application Control Engine Appliance.', 'Initial version of this MIB Added capability statement ciscoEnhancedSlbCapACSWV03R000 for Application Control Engine (ACE).',))
if mibBuilder.loadTexts: ciscoEnhancedSlbCapability.setLastUpdated('200807070000Z')
if mibBuilder.loadTexts: ciscoEnhancedSlbCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEnhancedSlbCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-slb@cisco.com')
if mibBuilder.loadTexts: ciscoEnhancedSlbCapability.setDescription('The capabilities description of CISCO-ENHANCED-SLB-MIB.')
ciscoEnhancedSlbCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 507, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapACSWV03R000 = ciscoEnhancedSlbCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapACSWV03R000 = ciscoEnhancedSlbCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoEnhancedSlbCapACSWV03R000.setDescription('ACSW (Application Control Software) 3.0 CISCO ENHANCED SLB MIB capabilities')
ciscoEnhancedSlbCapc4710aceVA1R70 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 507, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapc4710aceVA1R70 = ciscoEnhancedSlbCapc4710aceVA1R70.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapc4710aceVA1R70 = ciscoEnhancedSlbCapc4710aceVA1R70.setStatus('current')
if mibBuilder.loadTexts: ciscoEnhancedSlbCapc4710aceVA1R70.setDescription('ACSW (Application Control Software) A1(7) CISCO ENHANCED SLB MIB capabilities')
ciscoEnhancedSlbCapc4710aceVA3R10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 507, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapc4710aceVA3R10 = ciscoEnhancedSlbCapc4710aceVA3R10.setProductRelease('ACSW (Application Control Software) A3(1.0)\n                    for ACE 4710 Application Control Engine \n                    Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapc4710aceVA3R10 = ciscoEnhancedSlbCapc4710aceVA3R10.setStatus('current')
if mibBuilder.loadTexts: ciscoEnhancedSlbCapc4710aceVA3R10.setDescription('ACSW (Application Control Software) A3(1.0) CISCO ENHANCED SLB MIB capabilities')
mibBuilder.exportSymbols("CISCO-ENHANCED-SLB-CAPABILITY", PYSNMP_MODULE_ID=ciscoEnhancedSlbCapability, ciscoEnhancedSlbCapability=ciscoEnhancedSlbCapability, ciscoEnhancedSlbCapc4710aceVA1R70=ciscoEnhancedSlbCapc4710aceVA1R70, ciscoEnhancedSlbCapc4710aceVA3R10=ciscoEnhancedSlbCapc4710aceVA3R10, ciscoEnhancedSlbCapACSWV03R000=ciscoEnhancedSlbCapACSWV03R000)
