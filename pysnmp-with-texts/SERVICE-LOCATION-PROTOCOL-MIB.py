#
# PySNMP MIB module SERVICE-LOCATION-PROTOCOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SERVICE-LOCATION-PROTOCOL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:01:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibIdentifier, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, mib_2, IpAddress, Counter32, TimeTicks, Unsigned32, ObjectIdentity, NotificationType, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "mib-2", "IpAddress", "Counter32", "TimeTicks", "Unsigned32", "ObjectIdentity", "NotificationType", "Integer32", "Counter64")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
slpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 999))
if mibBuilder.loadTexts: slpMIB.setLastUpdated('200203010000Z')
if mibBuilder.loadTexts: slpMIB.setOrganization('SLP Project (at Source Forge)')
if mibBuilder.loadTexts: slpMIB.setContactInfo(' SLP Project (at Source Forge) Email: srvloc-discuss@lists.sourceforge.net Editor: Mark Bakke Postal: Cisco Systems Inc 6450 Wedgwood Road, Suite 130 Maple Grove, MN 55311 USA Tel: +1 763-398-1000 Email: mbakke@cisco.com Editor: Ira McDonald Postal: High North Inc 221 Ridge Ave Grand Marais, MI 49839 USA Tel: +1 906-494-2434 Email: imcdonald@sharplabs.com')
if mibBuilder.loadTexts: slpMIB.setDescription('The MIB module for monitoring (but not configuration) of SLP (Service Location Protocol) directory agents (DAs), service agents (SAs), and/or user agents (UAs) on managed systems.')
slpMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 1))
slpMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 2))
slpMIBObjectGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 2, 2))
class SlpAgentTypeTC(TextualConvention, Integer32):
    description = "The type of this SLP agent. See: 'net.slp.isDA' in SLP API (RFC 2614)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("da", 1), ("sa", 2), ("ua", 3))

class SlpScopeSourceTC(TextualConvention, Integer32):
    description = "The source (DHCP, etc) of this SLP scope or scope list. See: Section 2 'Introduction' in RFC 2610."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("static", 1), ("staticDA", 2), ("dhcp", 3), ("dhcpDA", 4), ("dynamicDA", 5), ("dynamicSA", 6), ("default", 7))

class SlpAttributeTypeTC(TextualConvention, Integer32):
    description = "The type of this SLP attribute. See: Section 5 'Service Attributes' in SLPv2 (RFC 2608)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("attrBoolean", 1), ("attrInteger", 2), ("attrString", 3), ("attrOpaque", 4), ("attrKeyword", 5))

slpAgent = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 1, 1))
slpAgentTable = MibTable((1, 3, 6, 1, 2, 1, 999, 1, 1, 1), )
if mibBuilder.loadTexts: slpAgentTable.setStatus('current')
if mibBuilder.loadTexts: slpAgentTable.setDescription('A table containing SLP (Service Location Protocol) objects for all of the SLP directory agents (DAs), service agents (SAs), or user agents (UAs) currently installed and (possibly) active on this managed system.')
slpAgentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1), ).setIndexNames((0, "SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentIndex"))
if mibBuilder.loadTexts: slpAgentEntry.setStatus('current')
if mibBuilder.loadTexts: slpAgentEntry.setDescription('An entry containing SLP (Service Location Protocol) objects for one of the SLP directory agents (DAs), service agents (SAs), or user agents (UAs) currently installed and (possibly) active on this managed system.')
slpAgentIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: slpAgentIndex.setStatus('current')
if mibBuilder.loadTexts: slpAgentIndex.setDescription("Ordinal of this conceptual row in 'slpAgentTable'.")
slpAgentSWInstalledIndexOrZero = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAgentSWInstalledIndexOrZero.setStatus('current')
if mibBuilder.loadTexts: slpAgentSWInstalledIndexOrZero.setDescription("The value of 'hrSWInstalledIndex' in the Host Resources MIB (RFC 2790) for the executable software for this SLP agent, or zero if none. See: 'hrSWInstalledIndex' in Host Resources MIB (RFC 2790).")
slpAgentName = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAgentName.setStatus('current')
if mibBuilder.loadTexts: slpAgentName.setDescription("The friendly locally unique name for this SLP agent, for use with remote network management scripts and GUIs For example 'daNewYork'.")
slpAgentType = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 4), SlpAgentTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAgentType.setStatus('current')
if mibBuilder.loadTexts: slpAgentType.setDescription("The type of this SLP agent (DA, SA, or UA). See: 'net.slp.isDA' in SLP API (RFC 2614).")
slpAgentIsBroadcastOnly = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAgentIsBroadcastOnly.setStatus('current')
if mibBuilder.loadTexts: slpAgentIsBroadcastOnly.setDescription("Broadcast only network enabled for this SLP agent. If 'true', SLP agent MUST send only broadcast messages. If 'false', SLP agent MAY send multicast messages. See: 'Broadcast Only' in section 14 of SLPv2 (RFC 2608). See: 'net.slp.isBroadcastOnly' in SLP API (RFC 2614).")
slpAgentActiveDADiscovery = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 6), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAgentActiveDADiscovery.setStatus('current')
if mibBuilder.loadTexts: slpAgentActiveDADiscovery.setDescription("Active DA discovery allowed for this SLP agent. If 'true', SLP agent MAY actively discover DAs, If 'false', SLP agent MUST NOT actively discover DAs. See: 'Active DA Discovery' in SLPv2 (RFC 2608). See: 'net.slp.DAActiveDiscoveryInterval' in SLP API (RFC2614).")
slpAgentPassiveDADiscovery = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 7), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAgentPassiveDADiscovery.setStatus('current')
if mibBuilder.loadTexts: slpAgentPassiveDADiscovery.setDescription("Passive DA discovery allowed for this SLP agent. If 'true', SLP agent MAY passively discover DAs, If 'false', SLP agent MUST NOT passively discover DAs. See: 'Passive DA Advertising' in SLPv2 (RFC 2608). See: 'net.slp.passiveDADetection' in SLP API (RFC2614).")
slpAgentMessageTypesSupported = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAgentMessageTypesSupported.setStatus('current')
if mibBuilder.loadTexts: slpAgentMessageTypesSupported.setDescription("The SLP message types supported by this SLP agent, expressed as an array of binary Function-ID values (RFC 2608). For example '0102'H means 'SrvRqst, SrvRply'. See: Section 8 'Required SLP Messages' in SLPv2 (RFC 2608).")
slpAgentExtensionsSupported = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAgentExtensionsSupported.setStatus('current')
if mibBuilder.loadTexts: slpAgentExtensionsSupported.setDescription("The SLP extensions supported by this SLP agent, expressed as an array of binary Extension ID values (RFC 2608), in network byte order (i.e., big-endian representation). For example '00020003'H means 'AttributeList, VendorOpaque'. See: Section 9.1 'SLP Extensions' in SLPv2 (RFC 2608).")
slpScope = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 1, 2))
slpScopeTable = MibTable((1, 3, 6, 1, 2, 1, 999, 1, 2, 1), )
if mibBuilder.loadTexts: slpScopeTable.setStatus('current')
if mibBuilder.loadTexts: slpScopeTable.setDescription("A table containing SLP (Service Location Protocol) objects for scope lists on this managed system. Usage: This table sparsely augments the 'slpAgentTable'. Usage: Scope lists consist of one or more rows in the 'slpScopeTable' (one row per scope value) for each SLP agent.")
slpScopeEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 1), ).setIndexNames((0, "SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentIndex"), (0, "SERVICE-LOCATION-PROTOCOL-MIB", "slpScopeIndex"))
if mibBuilder.loadTexts: slpScopeEntry.setStatus('current')
if mibBuilder.loadTexts: slpScopeEntry.setDescription('An entry containing SLP (Service Location Protocol) objects for one scope value on this managed system.')
slpScopeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: slpScopeIndex.setStatus('current')
if mibBuilder.loadTexts: slpScopeIndex.setDescription("Ordinal of this conceptual single row in 'slpScopeTable', subordinate to 'slpAgentIndex'.")
slpScopeSource = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 1, 2), SlpScopeSourceTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpScopeSource.setStatus('current')
if mibBuilder.loadTexts: slpScopeSource.setDescription("The source (DHCP, etc) of this SLP scope. See: Section 2 'Introduction' in RFC 2610.")
slpScopeValue = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpScopeValue.setStatus('current')
if mibBuilder.loadTexts: slpScopeValue.setDescription("One scope configured or discovered for this SLP agent. Note: The default (and lowest preference) scope value for any SLP agent is the string 'DEFAULT' verbatim in uppercase, per SLPv2 (RFC 2608). See: 'net.slp.useScopes' in SLP API (RFC 2614).")
slpAddress = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 1, 3))
slpAddressTable = MibTable((1, 3, 6, 1, 2, 1, 999, 1, 3, 1), )
if mibBuilder.loadTexts: slpAddressTable.setStatus('current')
if mibBuilder.loadTexts: slpAddressTable.setDescription("A table containing SLP (Service Location Protocol) objects for remote DA/SA address lists known to this managed system. Usage: This table sparsely augments the 'slpAgentTable'. Usage: DA/SA address lists consist of one or more rows in the 'slpAddressTable' (one row per address) for each SLP agent.")
slpAddressEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 1), ).setIndexNames((0, "SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentIndex"), (0, "SERVICE-LOCATION-PROTOCOL-MIB", "slpAddressIndex"))
if mibBuilder.loadTexts: slpAddressEntry.setStatus('current')
if mibBuilder.loadTexts: slpAddressEntry.setDescription('An entry containing SLP (Service Location Protocol) objects for one remote DA or SA address known to this managed system.')
slpAddressIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: slpAddressIndex.setStatus('current')
if mibBuilder.loadTexts: slpAddressIndex.setDescription("Ordinal of this conceptual single row in 'slpAddressTable', subordinate to 'slpAgentIndex'.")
slpAddressAgentType = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 1, 2), SlpAgentTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAddressAgentType.setStatus('current')
if mibBuilder.loadTexts: slpAddressAgentType.setDescription("The type of this remote SLP agent (DA or SA). See: 'net.slp.isDA' in SLP API (RFC 2614).")
slpAddressSource = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 1, 3), SlpScopeSourceTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAddressSource.setStatus('current')
if mibBuilder.loadTexts: slpAddressSource.setDescription("The source (DHCP, etc) of this remote SLP agent address. For example 'static(1)'. See: 'slpScopeSource' above in this SLP MIB.")
slpAddressOrName = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAddressOrName.setStatus('current')
if mibBuilder.loadTexts: slpAddressOrName.setDescription("Text formatted (dotted decimal) IPv4 address; or (per RFC 2373) text formatted (colon-delimited hexadecimal) IPv6 address; or a fully qualifed DNS name for this remote SLP agent (DA or SA). For example '13.281.11.12' or '3FFE:2A00:100:7031::1'. See: IP Version 6 Addressing Architecture (RFC 2373). See: Format for Literal IPv6 Addresses in URLs (RFC 2732). See: 'net.slp.DAAddresses' in SLP API (RFC 2614).")
slpAttribute = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 1, 4))
slpAttributeTable = MibTable((1, 3, 6, 1, 2, 1, 999, 1, 4, 1), )
if mibBuilder.loadTexts: slpAttributeTable.setStatus('current')
if mibBuilder.loadTexts: slpAttributeTable.setDescription("A table containing SLP (Service Location Protocol) objects for SLP agent (DA or SA) attribute lists on this managed system. Usage: This table sparsely augments the 'slpAgentTable' (UAs do not have attribute lists - DAs/SAs should have attribute lists with at least the SLP standard DA/SA attributes). Usage: Attribute lists consist of one or more rows in the 'slpAttributeTable' (one row per attribute) for each SLP agent.")
slpAttributeEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 1, 4, 1, 1), ).setIndexNames((0, "SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentIndex"), (0, "SERVICE-LOCATION-PROTOCOL-MIB", "slpAttributeIndex"))
if mibBuilder.loadTexts: slpAttributeEntry.setStatus('current')
if mibBuilder.loadTexts: slpAttributeEntry.setDescription("An entry containing SLP (Service Location Protocol) objects for one SLP agent (DA or SA) attribute on this managed system. See: 'net.slp.DAAttributes' in SLP API (RFC 2614). See: 'net.slp.SAAttributes' in SLP API (RFC 2614).")
slpAttributeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: slpAttributeIndex.setStatus('current')
if mibBuilder.loadTexts: slpAttributeIndex.setDescription("Ordinal of this conceptual single row in 'slpAttributeTable', subordinate to 'slpAgentIndex'.")
slpAttributeName = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 4, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAttributeName.setStatus('current')
if mibBuilder.loadTexts: slpAttributeName.setDescription("The name of this SLP attribute. For example 'printer-resolution-supported' in the 'service:printer' IANA registered service template. See: Section 5 'Service Attributes' in SLPv2 (RFC 2608).")
slpAttributeType = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 4, 1, 1, 3), SlpAttributeTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAttributeType.setStatus('current')
if mibBuilder.loadTexts: slpAttributeType.setDescription("The type of this SLP attribute. For example 'attrBoolean' for a string formatted boolean. See: Section 5 'Service Attributes' in SLPv2 (RFC 2608).")
slpAttributeValue = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 4, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAttributeValue.setStatus('current')
if mibBuilder.loadTexts: slpAttributeValue.setDescription("The value of this SLP attribute: a) A UTF-8 string if 'slpAttributeType' is 'attrBoolean', 'attrInteger', or 'attrString' b) an escaped string if 'slpAttributeType' is 'attrOpaque'; or c) an empty string if 'slpAttributeType' is 'attrKeyword'. See: Section 5 'Service Attributes' in SLPv2 (RFC 2608).")
slpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 999, 2, 1)).setObjects(("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentGroup"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpScopeGroup"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAddressGroup"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAttributeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    slpMIBCompliance = slpMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: slpMIBCompliance.setDescription('The compliance statements for SNMP Command Responders that implement the Service Location Protocol MIB.')
slpAgentGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 999, 2, 2, 1)).setObjects(("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentSWInstalledIndexOrZero"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentName"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentType"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentIsBroadcastOnly"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentActiveDADiscovery"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentPassiveDADiscovery"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentMessageTypesSupported"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentExtensionsSupported"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    slpAgentGroup = slpAgentGroup.setStatus('current')
if mibBuilder.loadTexts: slpAgentGroup.setDescription('The Agent object group in the SLP MIB')
slpScopeGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 999, 2, 2, 2)).setObjects(("SERVICE-LOCATION-PROTOCOL-MIB", "slpScopeSource"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpScopeValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    slpScopeGroup = slpScopeGroup.setStatus('current')
if mibBuilder.loadTexts: slpScopeGroup.setDescription('The Scope object group in the SLP MIB')
slpAddressGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 999, 2, 2, 3)).setObjects(("SERVICE-LOCATION-PROTOCOL-MIB", "slpAddressAgentType"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAddressSource"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAddressOrName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    slpAddressGroup = slpAddressGroup.setStatus('current')
if mibBuilder.loadTexts: slpAddressGroup.setDescription('The Address object group in the SLP MIB')
slpAttributeGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 999, 2, 2, 4)).setObjects(("SERVICE-LOCATION-PROTOCOL-MIB", "slpAttributeName"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAttributeType"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAttributeValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    slpAttributeGroup = slpAttributeGroup.setStatus('current')
if mibBuilder.loadTexts: slpAttributeGroup.setDescription('The Attribute object group in the SLP MIB')
mibBuilder.exportSymbols("SERVICE-LOCATION-PROTOCOL-MIB", slpScopeEntry=slpScopeEntry, slpAttributeIndex=slpAttributeIndex, slpScope=slpScope, slpAddressAgentType=slpAddressAgentType, slpAgentTable=slpAgentTable, slpAgentIsBroadcastOnly=slpAgentIsBroadcastOnly, slpAgentPassiveDADiscovery=slpAgentPassiveDADiscovery, slpMIBObjects=slpMIBObjects, slpAddressSource=slpAddressSource, slpMIBCompliance=slpMIBCompliance, slpAgentIndex=slpAgentIndex, SlpAgentTypeTC=SlpAgentTypeTC, SlpScopeSourceTC=SlpScopeSourceTC, slpAgentName=slpAgentName, slpAddressGroup=slpAddressGroup, slpScopeValue=slpScopeValue, slpAgentMessageTypesSupported=slpAgentMessageTypesSupported, slpAgentGroup=slpAgentGroup, slpScopeIndex=slpScopeIndex, slpAgentActiveDADiscovery=slpAgentActiveDADiscovery, slpAgentType=slpAgentType, slpAddressEntry=slpAddressEntry, slpAddressTable=slpAddressTable, SlpAttributeTypeTC=SlpAttributeTypeTC, slpScopeSource=slpScopeSource, slpMIBObjectGroups=slpMIBObjectGroups, slpAttributeTable=slpAttributeTable, slpAgentExtensionsSupported=slpAgentExtensionsSupported, slpAttributeGroup=slpAttributeGroup, slpScopeGroup=slpScopeGroup, slpAttributeValue=slpAttributeValue, slpAddressOrName=slpAddressOrName, slpAddress=slpAddress, slpMIBConformance=slpMIBConformance, PYSNMP_MODULE_ID=slpMIB, slpMIB=slpMIB, slpAttributeType=slpAttributeType, slpScopeTable=slpScopeTable, slpAgent=slpAgent, slpAgentEntry=slpAgentEntry, slpAddressIndex=slpAddressIndex, slpAttribute=slpAttribute, slpAttributeName=slpAttributeName, slpAgentSWInstalledIndexOrZero=slpAgentSWInstalledIndexOrZero, slpAttributeEntry=slpAttributeEntry)
