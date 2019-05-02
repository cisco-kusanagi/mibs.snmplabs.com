#
# PySNMP MIB module RBN-ATM-PROFILE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-ATM-PROFILE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:52:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
atmTrafficDescrParamEntry, = mibBuilder.importSymbols("ATM-MIB", "atmTrafficDescrParamEntry")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, TimeTicks, Integer32, iso, Counter64, Unsigned32, MibIdentifier, Counter32, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "Integer32", "iso", "Counter64", "Unsigned32", "MibIdentifier", "Counter32", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "ObjectIdentity")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
rbnAtmProfileMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 2))
if mibBuilder.loadTexts: rbnAtmProfileMIB.setLastUpdated('9807151645Z')
if mibBuilder.loadTexts: rbnAtmProfileMIB.setOrganization('RedBack Networks, Inc.')
if mibBuilder.loadTexts: rbnAtmProfileMIB.setContactInfo(' RedBack Networks, Inc. Postal: 1389 Moffett Park Drive Sunnyvale, CA 94089-1134 USA Phone: +1 408 548 3500 Fax: +1 408 548 3599 E-mail: mib-info@RedBackNetworks.com')
if mibBuilder.loadTexts: rbnAtmProfileMIB.setDescription('The MIB for instrumenting parameters associated with an ATM profile (traffic descriptor) beyond those instrumented by standards-track MIBs.')
class AtmProfileName(TextualConvention, OctetString):
    description = 'This data type is used to model an administratively assigned name as an identifier of an ATM profile.'
    status = 'current'
    displayHint = '80a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 80)

rbnAtmProfileMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 2, 1))
rbnAtmProfileTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1), )
if mibBuilder.loadTexts: rbnAtmProfileTable.setStatus('current')
if mibBuilder.loadTexts: rbnAtmProfileTable.setDescription('This table provides a collection of auxiliary objects providing parameters for atm profiles.')
rbnAtmProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1, 1), )
atmTrafficDescrParamEntry.registerAugmentions(("RBN-ATM-PROFILE-MIB", "rbnAtmProfileEntry"))
rbnAtmProfileEntry.setIndexNames(*atmTrafficDescrParamEntry.getIndexNames())
if mibBuilder.loadTexts: rbnAtmProfileEntry.setStatus('current')
if mibBuilder.loadTexts: rbnAtmProfileEntry.setDescription('Each entry in this table represents a profile.')
rbnAtmProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1, 1, 1), AtmProfileName().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnAtmProfileName.setStatus('current')
if mibBuilder.loadTexts: rbnAtmProfileName.setDescription('The textual handle assigned to an instance of the rbnAtmProfileTable (and via augmentation, the atmTrafficDescrParamTable). Using a textual handle instead of an arbitrary integer (such as atmTrafficDescrParamIndex) allows a configuration to contain human-friendly cross-references to the profiles from those places where they are used, such as in circuit configuration tables.')
rbnAtmCountersEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnAtmCountersEnabled.setStatus('current')
if mibBuilder.loadTexts: rbnAtmCountersEnabled.setDescription('An indication as to whether circuits configured with this profile should enable per-circuit statistical counters. An ATM circuit will only keep per-circuit statistical counters if this object is set to true(1) in the profile being used by the circuit.')
rbnAtmCellLossPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnAtmCellLossPriority.setStatus('current')
if mibBuilder.loadTexts: rbnAtmCellLossPriority.setDescription('An indication as to whether circuits configured with this profile should enable the Cell Loss Priority (CLP) bit on transmitted cells. If the profile being used by a circuit has this object set to true(1), then all cells transmitted on that circuit will have the CLP bit set.')
rbnAtmTransmitBuffers = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnAtmTransmitBuffers.setStatus('current')
if mibBuilder.loadTexts: rbnAtmTransmitBuffers.setDescription('This object limits the total number of outbound transmit packet buffers that may be consumed by the circuit that references the profile. Note well that this parameter should be used with caution. Improper setting can have severe consequences on overall system performance.')
rbnAtmProfileMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 2, 2))
rbnAtmProfileMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 2, 2, 1))
rbnAtmProfileMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 2, 2, 2))
rbnAtmProfileMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 2, 2, 2, 1)).setObjects(("RBN-ATM-PROFILE-MIB", "rbnAtmProfileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAtmProfileMIBCompliance = rbnAtmProfileMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: rbnAtmProfileMIBCompliance.setDescription('The compliance statement for RedBack Networks SNMP entities which represent AAL5 VCL statistics')
rbnAtmProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 2, 2, 1, 1)).setObjects(("RBN-ATM-PROFILE-MIB", "rbnAtmProfileName"), ("RBN-ATM-PROFILE-MIB", "rbnAtmCountersEnabled"), ("RBN-ATM-PROFILE-MIB", "rbnAtmCellLossPriority"), ("RBN-ATM-PROFILE-MIB", "rbnAtmTransmitBuffers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAtmProfileGroup = rbnAtmProfileGroup.setStatus('current')
if mibBuilder.loadTexts: rbnAtmProfileGroup.setDescription('A collection of objects providing supplemental AAL5 VCL information beyond that supplied by IETF standards-track MIBs')
mibBuilder.exportSymbols("RBN-ATM-PROFILE-MIB", rbnAtmProfileMIBObjects=rbnAtmProfileMIBObjects, rbnAtmProfileTable=rbnAtmProfileTable, rbnAtmProfileName=rbnAtmProfileName, rbnAtmCellLossPriority=rbnAtmCellLossPriority, rbnAtmProfileMIBCompliance=rbnAtmProfileMIBCompliance, AtmProfileName=AtmProfileName, rbnAtmTransmitBuffers=rbnAtmTransmitBuffers, rbnAtmCountersEnabled=rbnAtmCountersEnabled, rbnAtmProfileMIBConformance=rbnAtmProfileMIBConformance, PYSNMP_MODULE_ID=rbnAtmProfileMIB, rbnAtmProfileMIB=rbnAtmProfileMIB, rbnAtmProfileMIBCompliances=rbnAtmProfileMIBCompliances, rbnAtmProfileMIBGroups=rbnAtmProfileMIBGroups, rbnAtmProfileEntry=rbnAtmProfileEntry, rbnAtmProfileGroup=rbnAtmProfileGroup)
