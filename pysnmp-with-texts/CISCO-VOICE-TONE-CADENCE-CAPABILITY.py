#
# PySNMP MIB module CISCO-VOICE-TONE-CADENCE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-TONE-CADENCE-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:19:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
TimeTicks, Counter64, ModuleIdentity, NotificationType, ObjectIdentity, Integer32, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, iso, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Integer32", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "iso", "Bits", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVoiceToneCadenceCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 387))
ciscoVoiceToneCadenceCapability.setRevisions(('2004-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoiceToneCadenceCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVoiceToneCadenceCapability.setLastUpdated('200402020000Z')
if mibBuilder.loadTexts: ciscoVoiceToneCadenceCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoiceToneCadenceCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoVoiceToneCadenceCapability.setDescription('The agent capabilities for CISCO-VOICE-TONE-CADENCE-MIB.')
cVoiceToneCadenceCapV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 387, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoiceToneCadenceCapV5R00 = cVoiceToneCadenceCapV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoiceToneCadenceCapV5R00 = cVoiceToneCadenceCapV5R00.setStatus('current')
if mibBuilder.loadTexts: cVoiceToneCadenceCapV5R00.setDescription('CISCO-VOICE-TONE-CADENCE-MIB capabilities for VXSM in release 5.0.0.')
mibBuilder.exportSymbols("CISCO-VOICE-TONE-CADENCE-CAPABILITY", cVoiceToneCadenceCapV5R00=cVoiceToneCadenceCapV5R00, PYSNMP_MODULE_ID=ciscoVoiceToneCadenceCapability, ciscoVoiceToneCadenceCapability=ciscoVoiceToneCadenceCapability)
