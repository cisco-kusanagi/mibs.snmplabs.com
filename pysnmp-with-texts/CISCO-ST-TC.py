#
# PySNMP MIB module CISCO-ST-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ST-TC
# Produced by pysmi-0.3.4 at Wed May  1 11:53:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ciscoModules, = mibBuilder.importSymbols("CISCO-SMI", "ciscoModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, Integer32, Bits, ObjectIdentity, IpAddress, Counter64, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "Integer32", "Bits", "ObjectIdentity", "IpAddress", "Counter64", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "iso", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
storageTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 4))
storageTextualConventions.setRevisions(('2012-08-08 00:00', '2011-07-26 00:00', '2010-12-24 00:00', '2008-05-16 00:00', '2005-12-17 00:00', '2004-05-18 00:00', '2003-09-26 00:00', '2003-08-07 00:00', '2002-10-04 00:00', '2002-09-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: storageTextualConventions.setRevisionsDescriptions(('Added sixteenG and automaxSixteenG in fcIfSpeed', '-Added following enum to FcIfSpeed: autoMaxEightG.', '-Added following enums to FcIfSpeed: autoMax4G, eightG and tenG.', '-Added following enums to FcPortTypes TEXTUAL CONVENTION npPort, tfPort, tnpPort -Added following enums to InterfaceOperMode TEXTUAL CONVENTION. npPort, tfPort, tnpPort -Added following enums to FcPortModuleTypes TEXTUAL CONVENTION sfpDwdm, qsfp, x2Dwdm - Updated the description of the following objects: FcPortTxTypes, FcNameId.', '- Added following TCs FcIfSfpDiagLevelType FcIfServiceStateType - Added following enums in FcPortModuleTypes xfp, x2Short, x2Medium, x2Tall, xpakShort, xpakMedium, xpakTall and xenpak. - Added following enums in FcPortTxTypes. tenGigBaseSr, tenGigBaseLr, tenGigBaseEr, tenGigBaseLx4, tenGigBaseSw, tenGigBaseLw, tenGigBaseEw. - Added following enums in FcIfSpeed fourG and autoMaxTwoG.', "Added new textual convention 'InterfaceOperMode'.", 'Obtained the OID for this MIB.', 'Added stPort(15) to FcPortTypes.', 'Added fvPort and portOperDown to FcPortTypes. Added FcAddress and FcAddressType.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: storageTextualConventions.setLastUpdated('201208080000Z')
if mibBuilder.loadTexts: storageTextualConventions.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: storageTextualConventions.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 -NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: storageTextualConventions.setDescription('This module defines textual conventions used in Storage Area Network technology specific mibs.')
class VsanIndex(TextualConvention, Integer32):
    description = 'The VSAN id of a VSAN which uniquely identifies a VSAN within a fabric. VSAN id is 12-bit wide; so theoretically, 4096 VSANs can be defined in a fabric and this device can be part of. However, VSAN numbers 0 , 4094 and 4095 are reserved.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

class DomainId(TextualConvention, Integer32):
    description = 'The Domain Id of the switch. This is assigned dynamically if the Domain Manager is enabled on the switch or could be configured statically by the user.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 239)

class DomainIdOrZero(TextualConvention, Integer32):
    description = "The Textual convention is an extension to textual convetion 'DomainId'. It includes the value '0'in addition the range 1-239. Value '0' indicates that Domain Id has been neither configured nor assigned."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 239)

class FcAddressId(TextualConvention, OctetString):
    description = 'Represents Fibre Channel Address ID, a 24-bit value unique within the address space of a Fabric.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class FcNameId(TextualConvention, OctetString):
    reference = 'Fibre Channel Framing and Signaling (FC-FS) Rev 1.70 - Section 14 Name_Indentifier Formats.'
    description = 'Represents the World Wide Name (WWN) associated with a Fibre Channel (FC) entity. A WWN is a 64 bit address to uniquely identify each entity within a Fibre Channel fabric.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class FcNameIdOrZero(TextualConvention, OctetString):
    description = 'The World Wide Name (WWN) associated with a Fibre Channel (FC) entity. WWNs were initially defined as 64-bits in length. The latest definition (for future use) is 128-bits long. The zero-length string value is used in circumstances where the WWN is unassigned/unknown.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), )
class FcClassOfServices(TextualConvention, Bits):
    description = 'Represents the class of service capability of an NxPort or FxPort.'
    status = 'current'
    namedValues = NamedValues(("classF", 0), ("class1", 1), ("class2", 2), ("class3", 3), ("class4", 4), ("class5", 5), ("class6", 6))

class FcPortTypes(TextualConvention, Integer32):
    description = "Represents fibre channel port types: auto (1) - Mode is determined by port initialization scheme. fPort (2) - Fibre channel fabric port. flPort (3) - Fibre channel arbitrated loop port. ePort (4) - Fabric Expansion port. bPort (5) - Bridging port. fxPort (6) - This port can only be f_port or fl_port. sdPort (7) - SPAN destination port. SD_ports transmit traffic copied from one or more source ports for monitoring purposes. tlPort (8) - Translation loop port. nPort (9) - Fibre channel N port. nlPort (10) - Fibre channel NL port. nxPort (11) - This port can only be n_port or nl_port. -- read only port types. tePort (12) - Trunking e_port. Note: A port which is administratively set to 'ePort', will operationally have type 'tePort' if fcIfOperTrunkMode has the value 'trunk'. fvPort (13) - Virtual Port. portOperDown (14) - port operationally down If a port is operationally down, the port mode is unknown. In such cases the operational port mode is shown as 'portOperDown'. stPort (15) - SPAN Tunnel destination port. npPort (16) - N Proxy port mode applicable only to N-port Virtualizer (NPV) tfPort (17) - Trunking fibre channel fabric port. tnpPort (18) - Trunking N Proxy port mode applicable only to N-port Virtualizer (NPV)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("auto", 1), ("fPort", 2), ("flPort", 3), ("ePort", 4), ("bPort", 5), ("fxPort", 6), ("sdPort", 7), ("tlPort", 8), ("nPort", 9), ("nlPort", 10), ("nxPort", 11), ("tePort", 12), ("fvPort", 13), ("portOperDown", 14), ("stPort", 15), ("npPort", 16), ("tfPort", 17), ("tnpPort", 18))

class FcPortTxTypes(TextualConvention, Integer32):
    reference = 'IEEE Std 802.3-2005 carrier sense multiple access with collision detection (CSMA/CD) access method and physical layer specification.'
    description = 'Represents port transciever technology types. unknown (1) - unknown longWaveLaser (2) - 1550nm laser shortWaveLaser (3) - 850nm laser longWaveLaserCostReduced (4) - 1310nm laser electrical (5) - electrical tenGigBaseSr (6) - 10GBASE-SR 850nm laser tenGigBaseLr (7) - 10GBASE-LR 1310nm laser tenGigBaseEr (8) - 10GBASE-ER 1550nm laser tenGigBaseLx4 (9) - 10GBASE-LX4 WWDM 1300nm laser tenGigBaseSw (10) - 850nm laser tenGigBaseLw (11) - 1310nm laser tenGigBaseEw (12) - 1550nm laser .'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("unknown", 1), ("longWaveLaser", 2), ("shortWaveLaser", 3), ("longWaveLaserCostReduced", 4), ("electrical", 5), ("tenGigBaseSr", 6), ("tenGigBaseLr", 7), ("tenGigBaseEr", 8), ("tenGigBaseLx4", 9), ("tenGigBaseSw", 10), ("tenGigBaseLw", 11), ("tenGigBaseEw", 12))

class FcPortModuleTypes(TextualConvention, Integer32):
    description = 'Represents module type of the port connector. This object refers to the hardware implementation of the port. The enums are defined as per FC-GS-4 standard. unknown (1) - unknown other (2) - other gbic (3) - gbic (gigabit interface card) embedded (4) - gbic is part of the line card and is unremovable glm (5) - if its a gigabit link module (GLM). A GLM has a different form factor than GBIC. GLM is not supported by our switch. gbicWithSerialID (6) - If GBIC serial id can be read gbicWithoutSerialID (7) - If GBIC serial id cannot be read sfpWithSerialID (8) - If small form factor (SFP) pluggable GBICs serial id can be read sfpWithoutSerialID (9) - If small form factor (SFP) pluggable GBICs serial id cannot be read The following enums are module types for 10 gigabit small form factor pluggable sfp port connectors. xfp (10) - xfp x2Short (11) - x2 short x2Medium (12) - x2 medium x2Tall (13) - x2 tall xpakShort (14) - xpak short xpakMedium (15) - xpak medium xpakTall (16) - xpak tall xenpak (17) - xenpak sfpDwdm (18) - DWDM SFP type qsfp (19) - Quad small form-factor (QSFP) pluggable type x2Dwdm (20) - x2 DWDM .'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("gbic", 3), ("embedded", 4), ("glm", 5), ("gbicWithSerialID", 6), ("gbicWithoutSerialID", 7), ("sfpWithSerialID", 8), ("sfpWithoutSerialID", 9), ("xfp", 10), ("x2Short", 11), ("x2Medium", 12), ("x2Tall", 13), ("xpakShort", 14), ("xpakMedium", 15), ("xpakTall", 16), ("xenpak", 17), ("sfpDwdm", 18), ("qsfp", 19), ("x2Dwdm", 20))

class FcIfSpeed(TextualConvention, Integer32):
    description = 'Represents the speed of a fibre channel port. Following are the meanings of the enumerated values: auto (1) - Negotiate to determine the speed automatically. oneG (2) - 1Gbit twoG (3) - 2Gbit fourG (4) - 4Gbit autoMaxTwoG (5) - Negotiate to determine the speed automatically upto a maximum of 2Gbit. eightG (6) - 8Gbit autoMaxFourG (7) - Negotiate to determine the speed automatically upto a maximum of 4Gbit. tenG (8) - 10GBit. autoMaxEightG (9) - Negotiate to determine the speed automatically upto a maximum of 8Gbit. sixteenG (10) - 16GBit. autoMaxSixteenG (11) - Negotiate to determine the speed automatically upto a maximum of 16Gbit.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("auto", 1), ("oneG", 2), ("twoG", 3), ("fourG", 4), ("autoMaxTwoG", 5), ("eightG", 6), ("autoMaxFourG", 7), ("tenG", 8), ("autoMaxEightG", 9), ("sixteenG", 10), ("autoMaxSixteenG", 11))

class PortMemberList(TextualConvention, OctetString):
    description = "A list of ifIndex's of the ports that are members of this list. The value of this object is a concatenation of zero or more 4-octet strings, where each 4-octet string contains a 32-bit ifIndex value in network byte order. A zero length string value means this list has no members."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class FcAddress(TextualConvention, OctetString):
    description = 'Represents either the Fibre Channel Address ID or the World Wide Name associated with a Fibre Channel (FC) Entity.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(3, 3), ValueSizeConstraint(8, 8), )
class FcAddressType(TextualConvention, Integer32):
    description = 'Denotes if a Fibre Channel Address is a World Wide Name (WWN) or a Fibre Channel Address ID (FCID). wwn(1) - address is WWN. fcid(2) - address is FCID.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("wwn", 1), ("fcid", 2))

class InterfaceOperMode(TextualConvention, Integer32):
    description = "Represents the operational mode of an interface auto (1) - Mode is determined by port initialization scheme. fPort (2) - Fibre channel fabric port. flPort (3) - Fibre channel arbitrated loop port. ePort (4) - Fabric Expansion port. bPort (5) - Bridging port. fxPort (6) - This port can only be f_port or fl_port. sdPort (7) - SPAN destination port. SD_ports transmit traffic copied from one or more source ports for monitoring purposes. tlPort (8) - Translation loop port. nPort (9) - Fibre channel N port. nlPort (10) - Fibre channel NL port. nxPort (11) - This port can only be n_port or nl_port. -- read only port types. tePort (12) - Trunking e_port. Note: A port which is administratively set to 'ePort', will operationally have type 'tePort' if fcIfOperTrunkMode has the value 'trunk'. fvPort (13) - Virtual Port. portOperDown (14) - port operationally down If a port is operationally down, the port mode is unknown. In such cases the operational port mode is shown as 'portOperDown'. stPort (15) - SPAN Tunnel destination port. mgmtPort(16) - Mgmt Port. ipsPort(17) - Ethernet Port. evPort(18) - FCIP tunnels on Ethernet ports. npPort (19) - N Proxy port mode applicable only to N-port Virtualizer (NPV). tfPort (20) - Trunking fibre channel fabric port. tnpPort (21) - Trunking N Proxy port mode applicable only to N-port Virtualizer (NPV)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21))
    namedValues = NamedValues(("auto", 1), ("fPort", 2), ("flPort", 3), ("ePort", 4), ("bPort", 5), ("fxPort", 6), ("sdPort", 7), ("tlPort", 8), ("nPort", 9), ("nlPort", 10), ("nxPort", 11), ("tePort", 12), ("fvPort", 13), ("portOperDown", 14), ("stPort", 15), ("mgmtPort", 16), ("ipsPort", 17), ("evPort", 18), ("npPort", 19), ("tfPort", 20), ("tnpPort", 21))

class FcIfServiceStateType(TextualConvention, Integer32):
    description = 'Represents the service state of a Fibre Channel interface. Following are the meanings of the enumerated values: inService (1) - interface is in service and is allowed to become operational. outOfService (2) - interface is removed from service and is not allowed to become operational.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("inService", 1), ("outOfService", 2))

class FcIfSfpDiagLevelType(TextualConvention, Integer32):
    description = 'Represents the severity level of the SFP diagnostic information of an interface for temperature, voltage, current, optical transmit and receive power.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("normal", 2), ("lowWarning", 3), ("lowAlarm", 4), ("highWarning", 5), ("highAlarm", 6))

mibBuilder.exportSymbols("CISCO-ST-TC", FcPortModuleTypes=FcPortModuleTypes, FcIfSpeed=FcIfSpeed, FcClassOfServices=FcClassOfServices, PYSNMP_MODULE_ID=storageTextualConventions, FcNameId=FcNameId, FcNameIdOrZero=FcNameIdOrZero, DomainIdOrZero=DomainIdOrZero, FcAddressType=FcAddressType, FcAddress=FcAddress, DomainId=DomainId, FcPortTypes=FcPortTypes, PortMemberList=PortMemberList, FcIfServiceStateType=FcIfServiceStateType, FcAddressId=FcAddressId, FcPortTxTypes=FcPortTxTypes, storageTextualConventions=storageTextualConventions, FcIfSfpDiagLevelType=FcIfSfpDiagLevelType, VsanIndex=VsanIndex, InterfaceOperMode=InterfaceOperMode)
