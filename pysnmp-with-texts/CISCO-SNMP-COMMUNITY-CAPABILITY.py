#
# PySNMP MIB module CISCO-SNMP-COMMUNITY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SNMP-COMMUNITY-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:12:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
IpAddress, Integer32, Bits, ModuleIdentity, NotificationType, Unsigned32, TimeTicks, MibIdentifier, iso, Counter64, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "Bits", "ModuleIdentity", "NotificationType", "Unsigned32", "TimeTicks", "MibIdentifier", "iso", "Counter64", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSnmpCommunityCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 318))
ciscoSnmpCommunityCapability.setRevisions(('2008-08-04 00:00', '2006-03-29 00:00', '2004-01-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpCommunityCapability.setRevisionsDescriptions(('Added capability statement cSnmpCommunityCapc4710aceVA1R700 for ACE 4710 Application Control Engine Appliance.', 'Added capability statement cSnmpCommunityCapACSWV03R000 for Application Control Engine (ACE). Updated the conformance group name for cSnmpCommunityCapCatOSV06R0301 from snmpCommunityGroup to snmpCommunityTableGroup since the new version of SNMP-COMMUNITY-MIB (RFC3584) has changed the name to avoid conflicts with SNMPv2-MIB.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSnmpCommunityCapability.setLastUpdated('200808040000Z')
if mibBuilder.loadTexts: ciscoSnmpCommunityCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSnmpCommunityCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com, cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpCommunityCapability.setDescription('The capabilities description of SNMP-COMMUNITY-MIB.')
cSnmpCommunityCapCatOSV06R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 318, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapCatOSV06R0301 = cSnmpCommunityCapCatOSV06R0301.setProductRelease('Cisco CatOS 6.3(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapCatOSV06R0301 = cSnmpCommunityCapCatOSV06R0301.setStatus('current')
if mibBuilder.loadTexts: cSnmpCommunityCapCatOSV06R0301.setDescription('SNMP-COMMUNITY-MIB capabilities.')
cSnmpCommunityCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 318, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapACSWV03R000 = cSnmpCommunityCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapACSWV03R000 = cSnmpCommunityCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: cSnmpCommunityCapACSWV03R000.setDescription('SNMP-COMMUNITY-MIB capabilities.')
cSnmpCommunityCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 318, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapc4710aceVA1R700 = cSnmpCommunityCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapc4710aceVA1R700 = cSnmpCommunityCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: cSnmpCommunityCapc4710aceVA1R700.setDescription('SNMP-COMMUNITY-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SNMP-COMMUNITY-CAPABILITY", cSnmpCommunityCapCatOSV06R0301=cSnmpCommunityCapCatOSV06R0301, ciscoSnmpCommunityCapability=ciscoSnmpCommunityCapability, PYSNMP_MODULE_ID=ciscoSnmpCommunityCapability, cSnmpCommunityCapACSWV03R000=cSnmpCommunityCapACSWV03R000, cSnmpCommunityCapc4710aceVA1R700=cSnmpCommunityCapc4710aceVA1R700)
