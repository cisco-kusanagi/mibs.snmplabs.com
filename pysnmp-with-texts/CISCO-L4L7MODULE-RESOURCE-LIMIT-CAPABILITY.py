#
# PySNMP MIB module CISCO-L4L7MODULE-RESOURCE-LIMIT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-L4L7MODULE-RESOURCE-LIMIT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:04:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, MibIdentifier, IpAddress, Counter32, Bits, ModuleIdentity, NotificationType, Gauge32, Unsigned32, ObjectIdentity, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "MibIdentifier", "IpAddress", "Counter32", "Bits", "ModuleIdentity", "NotificationType", "Gauge32", "Unsigned32", "ObjectIdentity", "iso", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoL4L7ModRsrcLimCap = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 499))
ciscoL4L7ModRsrcLimCap.setRevisions(('2008-07-22 00:00', '2008-07-21 00:00', '2006-04-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoL4L7ModRsrcLimCap.setRevisionsDescriptions(('Added capability statement cL4L7ModRsrcLimCapc4710aceVA3R10 for ACE 4710 Application Control Engine Appliance A3(1.0).', 'Added VARIATION for crlRateLimitResourceMin object to cL4L7ModRsrcLimCapACSWV03R000 agent capability. Added capability statement cL4L7ModRsrcLimCapc4710aceVA1R700 for ACE 4710 Application Control Engine Appliance.', 'Added capability statement cL4L7ModRsrcLimCapACSWV03R000 for Application Control Engine (ACE).',))
if mibBuilder.loadTexts: ciscoL4L7ModRsrcLimCap.setLastUpdated('200807220000Z')
if mibBuilder.loadTexts: ciscoL4L7ModRsrcLimCap.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoL4L7ModRsrcLimCap.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-l47security@cisco.com')
if mibBuilder.loadTexts: ciscoL4L7ModRsrcLimCap.setDescription('The capabilities description for CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB.')
cL4L7ModRsrcLimCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 499, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapACSWV03R000 = cL4L7ModRsrcLimCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapACSWV03R000 = cL4L7ModRsrcLimCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: cL4L7ModRsrcLimCapACSWV03R000.setDescription('CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB capabilities.')
cL4L7ModRsrcLimCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 499, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapc4710aceVA1R700 = cL4L7ModRsrcLimCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                for ACE 4710 Application Control Engine \n                Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapc4710aceVA1R700 = cL4L7ModRsrcLimCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: cL4L7ModRsrcLimCapc4710aceVA1R700.setDescription('CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB capabilities.')
cL4L7ModRsrcLimCapc4710aceVA3R10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 499, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapc4710aceVA3R10 = cL4L7ModRsrcLimCapc4710aceVA3R10.setProductRelease('ACSW (Application Control Software) A3(1.0)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapc4710aceVA3R10 = cL4L7ModRsrcLimCapc4710aceVA3R10.setStatus('current')
if mibBuilder.loadTexts: cL4L7ModRsrcLimCapc4710aceVA3R10.setDescription('CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB capabilities for ACE 4710 Application Control Engine Appliance A3(1.0).')
mibBuilder.exportSymbols("CISCO-L4L7MODULE-RESOURCE-LIMIT-CAPABILITY", cL4L7ModRsrcLimCapc4710aceVA1R700=cL4L7ModRsrcLimCapc4710aceVA1R700, ciscoL4L7ModRsrcLimCap=ciscoL4L7ModRsrcLimCap, cL4L7ModRsrcLimCapc4710aceVA3R10=cL4L7ModRsrcLimCapc4710aceVA3R10, cL4L7ModRsrcLimCapACSWV03R000=cL4L7ModRsrcLimCapACSWV03R000, PYSNMP_MODULE_ID=ciscoL4L7ModRsrcLimCap)
