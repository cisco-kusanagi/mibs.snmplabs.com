#
# PySNMP MIB module ENTERASYS-ACTIVATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-ACTIVATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:03:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Integer32, Counter64, ModuleIdentity, Counter32, iso, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Integer32", "Counter64", "ModuleIdentity", "Counter32", "iso", "MibIdentifier", "IpAddress")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
etsysActivationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999))
etsysActivationMIB.setRevisions(('2002-04-18 14:54',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: etsysActivationMIB.setRevisionsDescriptions(('The initial version of this MIB module.',))
if mibBuilder.loadTexts: etsysActivationMIB.setLastUpdated('200204181454Z')
if mibBuilder.loadTexts: etsysActivationMIB.setOrganization('Enterasys Networks, Inc')
if mibBuilder.loadTexts: etsysActivationMIB.setContactInfo('Postal: Enterasys Networks, Inc. 500 Spaulding Turnpike P.O. Box 3060 Portsmouth, NH 03801 Phone: +1 603 501 5500 E-mail: support@enterasys.com WWW: http://www.enterasys.com')
if mibBuilder.loadTexts: etsysActivationMIB.setDescription("This MIB module defines a portion of the SNMP enterprise MIBs under Enterasys Networks' enterprise OID pertaining to configuration of product activation keys.")
etsysActivationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1))
class EnterasysKeyType(TextualConvention, Integer32):
    description = 'A value of this type indicates whether an activation key is a product key, or whether it is a special kind of key such as a demonstration key. noKey(1) Indicates that no key is configured. unknownKeyType(2) Indicates that a key is configured, but that the agent has no idea what type of key it is. productKey(3) Indicates that a product key is configured. demoKey(4) Indicates that a demonstration key is configured. Demonstration keys intended for customer use will typically have expirations or other restrictions.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("noKey", 1), ("unknownKeyType", 2), ("productKey", 3), ("demoKey", 4))

class EnterasysFeature(TextualConvention, Integer32):
    description = 'A value of this type identifies an optional feature for which an activation key may be bought or obtained. This enumeration type will be extended as necessary.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("dot1xAuthentication", 1), ("pointToMultipoint", 2))

etsysActivationBaseBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1))
etsysMaxActivationKeyRow = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMaxActivationKeyRow.setStatus('current')
if mibBuilder.loadTexts: etsysMaxActivationKeyRow.setDescription('The largest value that the agent supports for the index object etsysActivationKeyRow.')
etsysActivationKeyTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2), )
if mibBuilder.loadTexts: etsysActivationKeyTable.setStatus('current')
if mibBuilder.loadTexts: etsysActivationKeyTable.setDescription('This table contains activation keys for optional features.')
etsysActivationKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1), ).setIndexNames((0, "ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyRow"))
if mibBuilder.loadTexts: etsysActivationKeyEntry.setStatus('current')
if mibBuilder.loadTexts: etsysActivationKeyEntry.setDescription('Each valid conceptual row contains basic information about one product activation key. Only those rows for which the etsysActivationKeyStatus is active(1) may enable features. Note that it is possible for an active(1) row to contain a well-formatted, internally-consistent key that has expired. A managed system is under no obligation to enable features in response to the presence of expired keys.')
etsysActivationKeyRow = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: etsysActivationKeyRow.setStatus('current')
if mibBuilder.loadTexts: etsysActivationKeyRow.setDescription('An index that uniquely identifies a row in the product key table. Agents are not required to accept arbitrary indices -- they may limit indices to numbers in the range (1 - N), where N is defined as the maximum number of activation keys that can usefully be supported on a product.')
etsysActivationLicenseString = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysActivationLicenseString.setStatus('current')
if mibBuilder.loadTexts: etsysActivationLicenseString.setDescription("A place for human-readable administrative information associated with this activation key, such as a product serial number or a demo key's registration date. Some key formats may require entry of 'License String' values provided by the vendor. Agents may enforce the following rule with respect to such paired-key rows: ------------------------------------------------------- This object MUST be set before etsysActivationKeyStatus can become active(1), and MAY NOT be modified while etsysActivationKeyStatus is active(1). -------------------------------------------------------")
etsysActivationKeyValue = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysActivationKeyValue.setStatus('current')
if mibBuilder.loadTexts: etsysActivationKeyValue.setDescription("An activation key. The activation key must be coded as a string of printable characters. Spaces and hyphens are reserved punctuation characters. They may be used freely on input and output, and do not form part of the key value. (The agent is not required to preserve these or other non-essential aspects of the key formatting.) The key must conform to one of the meta-formats defined in this DESCRIPTION. These meta-formats are subject to change. Agents should validate activation keys at Set time. An agent may reject even a valid key if it is inapplicable to the managed device. This object MUST be set before etsysActivationKeyStatus can become active(1), and MAY NOT be modified while etsysActivationKeyStatus is active(1). ======================================================= Standard activation keys have the following format: <FormatCode> <OpaqueKey> The <FormatCode> is encoded as four hexadecimal digits, and identifies the format of the <OpaqueKey>. The <OpaqueKey> may be encoded in any fashion the agent likes, within the constraints mentioned earlier in this DESCRIPTION. ======================================================= A platform may accept keys of the format <Keyword> [Qualifiers] provided that there is no possibility of confusion with standard activation keys. This format is best suited to non-secret demo keys that are intended for a wide audience ('everyone reading the user manual'). ======================================================= Backwards compatibility example Task : Configure an existing RoamAbout AccessPoint 2000 P-MP activation key, using this MIB. <OpaqueKey> : XXXX-XXXX-XXXX-XXXX (existing key) <FormatCode> : 0001 You enter : 0001-XXXX-XXXX-XXXX-XXXX =======================================================")
etsysActivationKeyType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1, 4), EnterasysKeyType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysActivationKeyType.setStatus('current')
if mibBuilder.loadTexts: etsysActivationKeyType.setDescription('Derived from the activation key. Identifies the type of key (product key vs. demonstration key). Identification of existing demonstration keys may not be 100% accurate.')
etsysActivationKeyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysActivationKeyStatus.setStatus('current')
if mibBuilder.loadTexts: etsysActivationKeyStatus.setDescription('Supports creation, deletion, and activation of rows in the etsysActivationKeyTable. An instance of this variable may become active(1) only when there is a corresponding etsysActivationKeyValue. For some key formats, the etsysActivationLicenseString may need to be set to a matching vendor-supplied value. Note that a row with an active(1) status may contain a demo key that has expired, and that no longer provides access to any features.')
etsysActivationKeyFeatureTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 3), )
if mibBuilder.loadTexts: etsysActivationKeyFeatureTable.setStatus('current')
if mibBuilder.loadTexts: etsysActivationKeyFeatureTable.setDescription("This table indicates which optional feature or features each activation key enables. Rows only appear in this table for 'etsysActivationKeyValue' instances that contain recognizable key values.")
etsysActivationKeyFeatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 3, 1), ).setIndexNames((0, "ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyRow"), (0, "ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyFeature"))
if mibBuilder.loadTexts: etsysActivationKeyFeatureEntry.setStatus('current')
if mibBuilder.loadTexts: etsysActivationKeyFeatureEntry.setDescription('Each valid conceptual row indicates the existence of a known mapping between an activation key and an optional feature.')
etsysActivationKeyFeature = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 3, 1, 1), EnterasysFeature())
if mibBuilder.loadTexts: etsysActivationKeyFeature.setStatus('current')
if mibBuilder.loadTexts: etsysActivationKeyFeature.setDescription('Identifies one of the optional product features enabled by an activation key in the etsysActivationKeyTable.')
etsysActivationKeyRestrictions = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 3, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysActivationKeyRestrictions.setStatus('current')
if mibBuilder.loadTexts: etsysActivationKeyRestrictions.setDescription("If the activation key associated with this row is a demo key, this MIB object may contain a human-readable string describing the key's restrictions, expiration conditions, and/or status. A demo key that enables several features could, at least theoretically, have different conditions for each. Platforms may automatically enforce expirations, but are not guaranteed to do so. It is ultimately the system manager's responsibility to clean up expired keys. For a key that has no restrictions, this object's value may consist of the empty string, or of whitespace.")
etsysActivationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 2))
etsysActivationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 2, 1))
etsysActivationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 2, 2))
etsysActivationBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 2, 1, 1)).setObjects(("ENTERASYS-ACTIVATION-MIB", "etsysMaxActivationKeyRow"), ("ENTERASYS-ACTIVATION-MIB", "etsysActivationLicenseString"), ("ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyValue"), ("ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyType"), ("ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyStatus"), ("ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyRestrictions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysActivationBaseGroup = etsysActivationBaseGroup.setStatus('current')
if mibBuilder.loadTexts: etsysActivationBaseGroup.setDescription('A collection of objects for configuring activation keys for optional platform features.')
etsysActivationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 2, 2, 1)).setObjects(("ENTERASYS-ACTIVATION-MIB", "etsysActivationBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysActivationCompliance = etsysActivationCompliance.setStatus('current')
if mibBuilder.loadTexts: etsysActivationCompliance.setDescription('The compliance statement for devices that support the Enterasys Product Activation MIB.')
mibBuilder.exportSymbols("ENTERASYS-ACTIVATION-MIB", etsysActivationMIB=etsysActivationMIB, etsysActivationConformance=etsysActivationConformance, etsysActivationKeyRestrictions=etsysActivationKeyRestrictions, etsysActivationKeyValue=etsysActivationKeyValue, etsysActivationCompliance=etsysActivationCompliance, EnterasysFeature=EnterasysFeature, etsysActivationCompliances=etsysActivationCompliances, etsysActivationKeyRow=etsysActivationKeyRow, etsysActivationKeyFeatureTable=etsysActivationKeyFeatureTable, etsysActivationKeyEntry=etsysActivationKeyEntry, etsysActivationGroups=etsysActivationGroups, etsysActivationKeyTable=etsysActivationKeyTable, etsysActivationKeyFeatureEntry=etsysActivationKeyFeatureEntry, etsysActivationObjects=etsysActivationObjects, etsysActivationBaseGroup=etsysActivationBaseGroup, etsysActivationKeyStatus=etsysActivationKeyStatus, etsysActivationKeyFeature=etsysActivationKeyFeature, EnterasysKeyType=EnterasysKeyType, PYSNMP_MODULE_ID=etsysActivationMIB, etsysActivationBaseBranch=etsysActivationBaseBranch, etsysActivationKeyType=etsysActivationKeyType, etsysMaxActivationKeyRow=etsysMaxActivationKeyRow, etsysActivationLicenseString=etsysActivationLicenseString)
