#
# PySNMP MIB module CISCO-VOICE-CAS-MODULE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-CAS-MODULE-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:19:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibIdentifier, NotificationType, Gauge32, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Unsigned32, Integer32, iso, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "NotificationType", "Gauge32", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Unsigned32", "Integer32", "iso", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVoiceCasModuleCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 401))
ciscoVoiceCasModuleCapability.setRevisions(('2004-03-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoiceCasModuleCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVoiceCasModuleCapability.setLastUpdated('200403290000Z')
if mibBuilder.loadTexts: ciscoVoiceCasModuleCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoiceCasModuleCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoVoiceCasModuleCapability.setDescription('The capabilities description of CISCO-VOICE-CAS-MODULE-MIB.')
cvcmCapabilityV321 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 401, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcmCapabilityV321 = cvcmCapabilityV321.setProductRelease('Cisco VISM Release 3.2.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcmCapabilityV321 = cvcmCapabilityV321.setStatus('current')
if mibBuilder.loadTexts: cvcmCapabilityV321.setDescription('CISCO-VOICE-CAS-MODULE-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VOICE-CAS-MODULE-CAPABILITY", ciscoVoiceCasModuleCapability=ciscoVoiceCasModuleCapability, cvcmCapabilityV321=cvcmCapabilityV321, PYSNMP_MODULE_ID=ciscoVoiceCasModuleCapability)
