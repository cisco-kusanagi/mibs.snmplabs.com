#
# PySNMP MIB module CISCO-IP-PROTOCOL-FILTER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IP-PROTOCOL-FILTER-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:02:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Counter32, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, Bits, Gauge32, Integer32, NotificationType, iso, ObjectIdentity, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "Bits", "Gauge32", "Integer32", "NotificationType", "iso", "ObjectIdentity", "Counter64", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIpProtFilterCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 500))
ciscoIpProtFilterCapability.setRevisions(('2008-06-09 00:00', '2006-04-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIpProtFilterCapability.setRevisionsDescriptions(('Added capability statement cIpProtFilterCapc4710aceVA1R700 for ACE 4710 Application Control Engine Appliance.', 'Added capability statement cIpProtFilterCapACSWV03R000 for Application Control Engine (ACE).',))
if mibBuilder.loadTexts: ciscoIpProtFilterCapability.setLastUpdated('200806090000Z')
if mibBuilder.loadTexts: ciscoIpProtFilterCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIpProtFilterCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-dot11@cisco.com')
if mibBuilder.loadTexts: ciscoIpProtFilterCapability.setDescription('The capabilities description for CISCO-IP-PROTOCOL-FILTER-MIB.')
cIpProtFilterCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 500, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpProtFilterCapACSWV03R000 = cIpProtFilterCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpProtFilterCapACSWV03R000 = cIpProtFilterCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: cIpProtFilterCapACSWV03R000.setDescription('CISCO-IP-PROTOCOL-FILTER-MIB capabilities.')
cIpProtFilterCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 500, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpProtFilterCapc4710aceVA1R700 = cIpProtFilterCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                  for ACE 4710 Application Control Engine \n                  Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpProtFilterCapc4710aceVA1R700 = cIpProtFilterCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: cIpProtFilterCapc4710aceVA1R700.setDescription('CISCO-IP-PROTOCOL-FILTER-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IP-PROTOCOL-FILTER-CAPABILITY", PYSNMP_MODULE_ID=ciscoIpProtFilterCapability, cIpProtFilterCapACSWV03R000=cIpProtFilterCapACSWV03R000, ciscoIpProtFilterCapability=ciscoIpProtFilterCapability, cIpProtFilterCapc4710aceVA1R700=cIpProtFilterCapc4710aceVA1R700)
