#
# PySNMP MIB module CISCO-SLB-HEALTH-MON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SLB-HEALTH-MON-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:12:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
ObjectIdentity, iso, Counter32, NotificationType, Unsigned32, MibIdentifier, TimeTicks, Gauge32, IpAddress, Integer32, ModuleIdentity, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Counter32", "NotificationType", "Unsigned32", "MibIdentifier", "TimeTicks", "Gauge32", "IpAddress", "Integer32", "ModuleIdentity", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSlbHealthMonCapapbility = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 508))
ciscoSlbHealthMonCapapbility.setRevisions(('2008-07-03 00:00', '2008-02-08 00:00', '2006-06-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSlbHealthMonCapapbility.setRevisionsDescriptions(('Added ciscoSlbHealthMonCapc4710aceVA3R100 agent capabilities for ACE 4710 Application Control Engine Appliance.', 'Added ciscoSlbHealthMonCapc4710aceVA1R700 agent capabilities for ACE 4710 Application Control Engine Appliance.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSlbHealthMonCapapbility.setLastUpdated('200807030000Z')
if mibBuilder.loadTexts: ciscoSlbHealthMonCapapbility.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSlbHealthMonCapapbility.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-slb@cisco.com')
if mibBuilder.loadTexts: ciscoSlbHealthMonCapapbility.setDescription('The capabilities description of CISCO-SLB-HEALTH-MON-MIB.')
ciscoSlbHealthMonCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 508, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapabilityACSWV03R000 = ciscoSlbHealthMonCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapabilityACSWV03R000 = ciscoSlbHealthMonCapabilityACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbHealthMonCapabilityACSWV03R000.setDescription('CISCO-SLB-HEALTH-MON-MIB capabilities.')
ciscoSlbHealthMonCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 508, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapc4710aceVA1R700 = ciscoSlbHealthMonCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                for ACE 4710 Application Control Engine \n                Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapc4710aceVA1R700 = ciscoSlbHealthMonCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbHealthMonCapc4710aceVA1R700.setDescription('CISCO-SLB-HEALTH-MON-MIB capabilities.')
ciscoSlbHealthMonCapc4710aceVA3R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 508, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapc4710aceVA3R100 = ciscoSlbHealthMonCapc4710aceVA3R100.setProductRelease('ACSW (Application Control Software) A3(1.0)\n                for ACE 4710 Application Control Engine \n                Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapc4710aceVA3R100 = ciscoSlbHealthMonCapc4710aceVA3R100.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbHealthMonCapc4710aceVA3R100.setDescription('CISCO-SLB-HEALTH-MON-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SLB-HEALTH-MON-CAPABILITY", ciscoSlbHealthMonCapapbility=ciscoSlbHealthMonCapapbility, ciscoSlbHealthMonCapc4710aceVA1R700=ciscoSlbHealthMonCapc4710aceVA1R700, PYSNMP_MODULE_ID=ciscoSlbHealthMonCapapbility, ciscoSlbHealthMonCapabilityACSWV03R000=ciscoSlbHealthMonCapabilityACSWV03R000, ciscoSlbHealthMonCapc4710aceVA3R100=ciscoSlbHealthMonCapc4710aceVA3R100)
