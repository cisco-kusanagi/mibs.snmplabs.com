#
# PySNMP MIB module ENERGY-OBJECT-CONTEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENERGY-OBJECT-CONTEXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:02:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
IANAEnergyRelationship, = mibBuilder.importSymbols("IANA-ENERGY-RELATION-MIB", "IANAEnergyRelationship")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, NotificationType, Unsigned32, Gauge32, IpAddress, Counter32, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, TimeTicks, Bits, iso, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Unsigned32", "Gauge32", "IpAddress", "Counter32", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "TimeTicks", "Bits", "iso", "Counter64", "Integer32")
StorageType, DisplayString, RowStatus, TextualConvention, TruthValue, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "DisplayString", "RowStatus", "TextualConvention", "TruthValue", "MacAddress")
UUIDorZero, = mibBuilder.importSymbols("UUID-TC-MIB", "UUIDorZero")
energyObjectContextMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 231))
energyObjectContextMIB.setRevisions(('2015-02-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: energyObjectContextMIB.setRevisionsDescriptions(('Initial version, published as RFC 7461.',))
if mibBuilder.loadTexts: energyObjectContextMIB.setLastUpdated('201502090000Z')
if mibBuilder.loadTexts: energyObjectContextMIB.setOrganization('IETF EMAN Working Group')
if mibBuilder.loadTexts: energyObjectContextMIB.setContactInfo('WG Charter: http://datatracker.ietf.org/wg/eman/charter/ Mailing Lists: General Discussion: eman@ietf.org To Subscribe: https://www.ietf.org/mailman/listinfo/eman Archive: http://www.ietf.org/mail-archive/web/eman Editors: John Parello Cisco Systems, Inc. 3550 Cisco Way San Jose, California 95134 United States Phone: +1 408 525 2339 Email: jparello@cisco.com Benoit Claise Cisco Systems, Inc. De Kleetlaan 6a b1 Degem 1831 Belgium Phone: +32 2 704 5622 Email: bclaise@cisco.com Mouli Chandramouli Cisco Systems, Inc. Sarjapur Outer Ring Road Bangalore 560103 India Phone: +91 80 4429 2409 Email: moulchan@cisco.com')
if mibBuilder.loadTexts: energyObjectContextMIB.setDescription("Copyright (c) 2015 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info). This MIB is used for describing the identity and the context information of Energy Objects.")
energyObjectContextMIBNotifs = MibIdentifier((1, 3, 6, 1, 2, 1, 231, 0))
energyObjectContextMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 231, 1))
energyObjectContextMIBConform = MibIdentifier((1, 3, 6, 1, 2, 1, 231, 2))
class PethPsePortIndexOrZero(TextualConvention, Integer32):
    description = 'This textual convention is an extension of the pethPsePortIndex convention, which defines a greater- than-zero value used to identify a power Ethernet Power Sourcing Equipment (PSE) port. This extension permits the additional value of zero. The semantics of the value zero are object-specific and must, therefore, be defined as part of the description of any object that uses this syntax. Examples of the usage of this extension are situations where none or all physical entities need to be referenced.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class PethPsePortGroupIndexOrZero(TextualConvention, Integer32):
    description = 'This textual convention is an extension of the pethPsePortGroupIndex convention from the Power Over Ethernet MIB in RFC 3621, which defines a greater-than-zero value used to identify the group containing the port to which a power Ethernet PSE is connected. This extension permits the additional value of zero. The semantics of the value zero are object-specific and must, therefore, be defined as part of the description of any object that uses this syntax. Examples of the usage of this extension are situations where none or all physical entities need to be referenced.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class LldpPortNumberOrZero(TextualConvention, Integer32):
    description = 'This textual convention is an extension of the LldpPortNumber convention specified in the LLDP MIB, which defines a greater than zero value used to uniquely identify each port contained in the chassis (that is known to the LLDP agent) by a port number. This extension permits the additional value of zero. The semantics of the value zero are object-specific and must, therefore, be defined as part of the description of any object that uses this syntax. Examples of the usage of this extension are situations where none or all physical entities need to be referenced.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4096)

class EnergyObjectKeywordList(TextualConvention, OctetString):
    description = "A list of keywords that can be used to group Energy Objects for reporting or searching. If multiple keywords are present, then this string will contain all the keywords separated by the ',' character. All alphanumeric characters and symbols (other than a comma), such as #, (, $, !, and &, are allowed. White spaces before and after the commas are ignored, as well as within a keyword itself. For example, if an Energy Object were to be tagged with the keyword values 'hospitality' and 'guest', then the keyword list will be 'hospitality,guest'."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 2048)

eoTable = MibTable((1, 3, 6, 1, 2, 1, 231, 1, 1), )
if mibBuilder.loadTexts: eoTable.setStatus('current')
if mibBuilder.loadTexts: eoTable.setDescription('This table lists Energy Objects.')
eoEntry = MibTableRow((1, 3, 6, 1, 2, 1, 231, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: eoEntry.setStatus('current')
if mibBuilder.loadTexts: eoEntry.setDescription('An entry describes the attributes of an Energy Object. Whenever a new Energy Object is added or an existing Energy Object is deleted, a row in the eoTable is added or deleted.')
eoEthPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 1), PethPsePortIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoEthPortIndex.setReference('RFC 3621: Power Ethernet MIB')
if mibBuilder.loadTexts: eoEthPortIndex.setStatus('current')
if mibBuilder.loadTexts: eoEthPortIndex.setDescription('This variable uniquely identifies the power Ethernet port to which a Power over Ethernet device is connected. If the Power over Ethernet MIB in RFC 3621 is supported by the SNMP agent managing the Energy Object, then the Energy Object eoethPortIndex MUST contain the corresponding value of pethPsePortIndex. If such a power Ethernet port cannot be specified or is not known, then the object is zero.')
eoEthPortGrpIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 2), PethPsePortGroupIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoEthPortGrpIndex.setReference('RFC 3621: Power Ethernet MIB')
if mibBuilder.loadTexts: eoEthPortGrpIndex.setStatus('current')
if mibBuilder.loadTexts: eoEthPortGrpIndex.setDescription('This variable uniquely identifies the group containing the port to which a power over Ethernet device PSE is connected (RFC 3621). If the Power over Ethernet MIB (RFC 3621) is supported by the SNMP agent managing the Energy Object, then the Energy Object eoEthPortGrpIndex MUST contain the corresponding value of eoethPortGrpIndex. If such a power Ethernet port cannot be specified or is not known, then the object is zero.')
eoLldpPortNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 3), LldpPortNumberOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoLldpPortNumber.setReference('LLDP MIB, IEEE 802.1AB-2005; LLDP-MED-MIB, ANSI/TIA-1057')
if mibBuilder.loadTexts: eoLldpPortNumber.setStatus('current')
if mibBuilder.loadTexts: eoLldpPortNumber.setDescription('This variable uniquely identifies the port component (contained in the local chassis with the LLDP agent) as defined by the lldpLocPortNum in the LLDP-MIB and LLDP-MED-MIB. If the LLDP-MIB is supported by the SNMP agent managing the Energy Object, then the Energy Object eoLldpPortNumber MUST contain the corresponding value of lldpLocPortNum from the LLDP-MIB. If such a port number cannot be specified or is not known, then the object is zero.')
eoMgmtMacAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoMgmtMacAddress.setStatus('current')
if mibBuilder.loadTexts: eoMgmtMacAddress.setDescription('This object specifies a Media Access Control (MAC) address of the Energy Object.')
eoMgmtAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoMgmtAddressType.setStatus('current')
if mibBuilder.loadTexts: eoMgmtAddressType.setDescription('This object specifies the eoMgmtAddress type, i.e., an IPv4 or IPv6 address. This object MUST be populated when eoMgmtAddress is populated.')
eoMgmtAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 6), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoMgmtAddress.setStatus('current')
if mibBuilder.loadTexts: eoMgmtAddress.setDescription('This object specifies the management address as an IPv4 address or IPv6 address of Energy Object. The IP address type, i.e. IPv4 or IPv6, is determined by the eoMgmtAddressType value. This object can be used as an alternate key to help link the Energy Object with other keyed information that may be stored within the EnMS(s).')
eoMgmtDNSName = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoMgmtDNSName.setReference('RFC 1034: Domain names - concepts and facilities, Section 3.1.')
if mibBuilder.loadTexts: eoMgmtDNSName.setStatus('current')
if mibBuilder.loadTexts: eoMgmtDNSName.setDescription('This object specifies a DNS name of the eoMgmtAddress. This object can be used as an alternate key to help link the Energy Object with other keyed information that may be stored within the EnMS(s). A DNS Name must always be a fully qualified name. This MIB uses the same encoding as the DNS protocol.')
eoDomainName = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 8), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eoDomainName.setStatus('current')
if mibBuilder.loadTexts: eoDomainName.setDescription('This object specifies the name of an Energy Management Domain for the Energy Object. By default, this object should be an empty string. The value of eoDomainName must remain constant at least from one re-initialization of the entity local management system to the next re- initialization.')
eoRoleDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 9), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eoRoleDescription.setStatus('current')
if mibBuilder.loadTexts: eoRoleDescription.setDescription("This object specifies an administratively assigned name to indicate the purpose an Energy Object serves in the network. For example, we can have a phone deployed to a lobby with eoRoleDescription as 'Lobby phone'. This object specifies that the value is the zero-length string value if no role description is configured. The value of eoRoleDescription must remain constant at least from one re-initialization of the entity local management system to the next re-initialization.")
eoKeywords = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 10), EnergyObjectKeywordList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eoKeywords.setStatus('current')
if mibBuilder.loadTexts: eoKeywords.setDescription("This object specifies a list of keywords that can be used to group Energy Objects for reporting or searching. The value is the zero-length string if no keywords have been configured. If multiple keywords are present, then this string will contain all the keywords separated by the ',' character. For example, if an Energy Object were to be tagged with the keyword values 'hospitality' and 'guest', then the keyword list will be 'hospitality,guest'. If write access is implemented and a value is written into the instance, the agent must retain the supplied value in the eoKeywords instance associated with the same physical entity for as long as that entity remains instantiated. This includes instantiations across all re-initializations/reboots of the local management agent.")
eoImportance = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eoImportance.setStatus('current')
if mibBuilder.loadTexts: eoImportance.setDescription('This object specifies a ranking of how important the Energy Object is (on a scale of 1 to 100) compared with other Energy Objects in the same Energy Management Domain. The ranking should provide a business or operational context for the Energy Object as compared to other similar Energy Objects. This ranking could be used as input for policy-based network management. Although network managers must establish their own ranking, the following is a broad recommendation: 90 to 100 Emergency response 80 to 89 Executive or business critical 70 to 79 General or average 60 to 69 Staff or support 40 to 59 Public or guest 1 to 39 Decorative or hospitality The value of eoImportance must remain constant at least from one re-initialization of the Energy Object local management system to the next re-initialization.')
eoPowerCategory = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("consumer", 0), ("producer", 1), ("meter", 2), ("distributor", 3), ("store", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoPowerCategory.setStatus('current')
if mibBuilder.loadTexts: eoPowerCategory.setDescription('This object describes the Energy Object category, which indicates the expected behavior or physical property of the Energy Object, based on its design. An Energy Object can be a consumer(0), producer(1), meter(2), distributor(3), or store(4). In some cases, a meter is required to measure the power consumption. In such a case, this meter Energy Object category is meter(2). If a device is distributing electric Energy, the category of the Energy Object is distributor (3). If a device is storing electric Energy, the category of the device can be store (4).')
eoAlternateKey = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 13), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eoAlternateKey.setStatus('current')
if mibBuilder.loadTexts: eoAlternateKey.setDescription('The eoAlternateKey object specifies an alternate key string that can be used to identify the Energy Object. Since Energy Management Systems (EnMS) and Network Management Systems (NMSs) may need to correlate objects across management systems, this alternate key is provided to provide such a link. This optional value is intended as a foreign key or alternate identifier for a manufacturer or EnMS/NMS to use to correlate the unique Energy Object Id in other systems or namespaces. If an alternate key is not available or is not applicable, then the value is the zero-length string. The value of eoAlternateKey must remain constant at least from one re-initialization of the entity local management system to the next re-initialization.')
eoPowerInterfaceType = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("inlet", 0), ("outlet", 1), ("both", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoPowerInterfaceType.setStatus('current')
if mibBuilder.loadTexts: eoPowerInterfaceType.setDescription('This object describes the Power Interface for an Energy Object. A Power Interface is an interface at which an Energy Object is connected to a power transmission medium, at which it can in turn receive power, provide power, or both. A Power Interface type can be an inlet(0), an outlet(1), or both(2), respectively.')
eoRelationTable = MibTable((1, 3, 6, 1, 2, 1, 231, 1, 2), )
if mibBuilder.loadTexts: eoRelationTable.setStatus('current')
if mibBuilder.loadTexts: eoRelationTable.setDescription('This table describes the relationships between Energy Objects.')
eoRelationEntry = MibTableRow((1, 3, 6, 1, 2, 1, 231, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "ENERGY-OBJECT-CONTEXT-MIB", "eoRelationIndex"))
if mibBuilder.loadTexts: eoRelationEntry.setReference(' RFC 7326: Energy Management Framework')
if mibBuilder.loadTexts: eoRelationEntry.setStatus('current')
if mibBuilder.loadTexts: eoRelationEntry.setDescription('An entry in this table specifies the Energy relationship between Energy objects. Energy relations between two Energy objects are defined in RFC 7326.')
eoRelationIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: eoRelationIndex.setStatus('current')
if mibBuilder.loadTexts: eoRelationIndex.setDescription('This object is an arbitrary index to identify the Energy Object related to another Energy Object.')
eoRelationID = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 2, 1, 2), UUIDorZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eoRelationID.setReference('RFC 6933: Entity MIB (Version 4)')
if mibBuilder.loadTexts: eoRelationID.setStatus('current')
if mibBuilder.loadTexts: eoRelationID.setDescription('This object specifies the Universally Unique Identifier (UUID) of the peer (other) Energy Object. The UUID must comply with the specifications of UUID in UUID-TC-MIB. If the UUID of the Energy Object is unknown or nonexistent, the eoRelationID will be set to a zero-length string instead. It is preferable that the value of entPhysicalUUID from ENTITY-MIB is used for values for this object.')
eoRelationship = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 2, 1, 3), IANAEnergyRelationship()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eoRelationship.setStatus('current')
if mibBuilder.loadTexts: eoRelationship.setDescription('This object describes the relations between Energy Objects. For each Energy Object, the relations between the other Energy Objects are specified using the bitmap.')
eoRelationStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eoRelationStatus.setStatus('current')
if mibBuilder.loadTexts: eoRelationStatus.setDescription('The status controls and reflects the creation and activation status of a row in this table to specify energy relationship between Energy Objects. An entry status may not be active(1) unless all objects in the entry have the appropriate values. No attempt to modify a row columnar object instance value in the eoRelationTable should be issued while the value of eoRelationStatus is active(1). The data can be destroyed by setting up the eoRelationStatus to destroy(2).')
eoRelationStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 2, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eoRelationStorageType.setStatus('current')
if mibBuilder.loadTexts: eoRelationStorageType.setDescription('This variable indicates the storage type for this row.')
energyObjectContextMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 231, 2, 1))
energyObjectContextMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 231, 2, 2))
energyObjectContextMIBFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 231, 2, 1, 1)).setObjects(("ENERGY-OBJECT-CONTEXT-MIB", "energyObjectContextMIBTableGroup"), ("ENERGY-OBJECT-CONTEXT-MIB", "energyObjectRelationTableGroup"), ("ENERGY-OBJECT-CONTEXT-MIB", "energyObjectOptionalMIBTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    energyObjectContextMIBFullCompliance = energyObjectContextMIBFullCompliance.setStatus('current')
if mibBuilder.loadTexts: energyObjectContextMIBFullCompliance.setDescription('When this MIB is implemented with support for read-write, then such an implementation can claim full compliance. Such devices can then be both monitored and configured with this MIB. Module Compliance of ENTITY-MIB with respect to entity4CRCompliance MUST be supported.')
energyObjectContextMIBReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 231, 2, 1, 2)).setObjects(("ENERGY-OBJECT-CONTEXT-MIB", "energyObjectContextMIBTableGroup"), ("ENERGY-OBJECT-CONTEXT-MIB", "energyObjectRelationTableGroup"), ("ENERGY-OBJECT-CONTEXT-MIB", "energyObjectOptionalMIBTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    energyObjectContextMIBReadOnlyCompliance = energyObjectContextMIBReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: energyObjectContextMIBReadOnlyCompliance.setDescription('When this MIB is implemented without support for read-write (i.e., in read-only mode), then such an implementation can claim read-only compliance. Such a device can then be monitored but cannot be configured with this MIB. Module Compliance of ENTITY-MIB with respect to entity4CRCompliance MUST be supported.')
energyObjectContextMIBTableGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 231, 2, 2, 1)).setObjects(("ENERGY-OBJECT-CONTEXT-MIB", "eoDomainName"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoRoleDescription"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoAlternateKey"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoKeywords"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoImportance"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoPowerCategory"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoPowerInterfaceType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    energyObjectContextMIBTableGroup = energyObjectContextMIBTableGroup.setStatus('current')
if mibBuilder.loadTexts: energyObjectContextMIBTableGroup.setDescription('This group contains the collection of all the objects related to the EnergyObject.')
energyObjectOptionalMIBTableGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 231, 2, 2, 2)).setObjects(("ENERGY-OBJECT-CONTEXT-MIB", "eoEthPortIndex"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoEthPortGrpIndex"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoLldpPortNumber"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoMgmtMacAddress"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoMgmtAddressType"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoMgmtAddress"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoMgmtDNSName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    energyObjectOptionalMIBTableGroup = energyObjectOptionalMIBTableGroup.setStatus('current')
if mibBuilder.loadTexts: energyObjectOptionalMIBTableGroup.setDescription('This group contains the collection of all the objects related to the Energy Object.')
energyObjectRelationTableGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 231, 2, 2, 3)).setObjects(("ENERGY-OBJECT-CONTEXT-MIB", "eoRelationID"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoRelationship"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoRelationStatus"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoRelationStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    energyObjectRelationTableGroup = energyObjectRelationTableGroup.setStatus('current')
if mibBuilder.loadTexts: energyObjectRelationTableGroup.setDescription('This group contains the collection of all objects specifying the relationship between Energy Objects.')
mibBuilder.exportSymbols("ENERGY-OBJECT-CONTEXT-MIB", energyObjectContextMIBTableGroup=energyObjectContextMIBTableGroup, eoMgmtDNSName=eoMgmtDNSName, eoPowerInterfaceType=eoPowerInterfaceType, eoRelationTable=eoRelationTable, energyObjectContextMIBReadOnlyCompliance=energyObjectContextMIBReadOnlyCompliance, PethPsePortIndexOrZero=PethPsePortIndexOrZero, eoAlternateKey=eoAlternateKey, eoPowerCategory=eoPowerCategory, eoMgmtMacAddress=eoMgmtMacAddress, energyObjectContextMIBObjects=energyObjectContextMIBObjects, energyObjectContextMIBCompliances=energyObjectContextMIBCompliances, eoRoleDescription=eoRoleDescription, eoKeywords=eoKeywords, energyObjectContextMIBConform=energyObjectContextMIBConform, energyObjectContextMIBFullCompliance=energyObjectContextMIBFullCompliance, energyObjectRelationTableGroup=energyObjectRelationTableGroup, energyObjectContextMIBGroups=energyObjectContextMIBGroups, eoRelationIndex=eoRelationIndex, eoMgmtAddress=eoMgmtAddress, eoEthPortIndex=eoEthPortIndex, energyObjectContextMIB=energyObjectContextMIB, eoEthPortGrpIndex=eoEthPortGrpIndex, eoLldpPortNumber=eoLldpPortNumber, EnergyObjectKeywordList=EnergyObjectKeywordList, energyObjectContextMIBNotifs=energyObjectContextMIBNotifs, eoEntry=eoEntry, PethPsePortGroupIndexOrZero=PethPsePortGroupIndexOrZero, eoDomainName=eoDomainName, PYSNMP_MODULE_ID=energyObjectContextMIB, LldpPortNumberOrZero=LldpPortNumberOrZero, eoRelationID=eoRelationID, energyObjectOptionalMIBTableGroup=energyObjectOptionalMIBTableGroup, eoRelationStatus=eoRelationStatus, eoRelationship=eoRelationship, eoMgmtAddressType=eoMgmtAddressType, eoRelationStorageType=eoRelationStorageType, eoRelationEntry=eoRelationEntry, eoImportance=eoImportance, eoTable=eoTable)
