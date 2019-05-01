#
# PySNMP MIB module HH3C-FC-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-FC-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:26:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Gauge32, Integer32, Counter64, IpAddress, TimeTicks, iso, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "Integer32", "Counter64", "IpAddress", "TimeTicks", "iso", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Bits", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class Hh3cFcAddressType(TextualConvention, Integer32):
    description = 'Identifies Fibre Channel address type, World Wide Name or Fibre Channel ID.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("wwn", 1), ("fcid", 2))

class Hh3cFcAddress(TextualConvention, OctetString):
    description = 'Represents either the Fibre Channel ID or the World Wide Name associated with a Fibre Channel entity.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(3, 3), ValueSizeConstraint(8, 8), )
class Hh3cFcAddressId(TextualConvention, OctetString):
    description = 'Represents Fibre Channel ID, a 24-bit value unique within the address space of a fabric.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class Hh3cFcAddressIdOrZero(TextualConvention, OctetString):
    description = 'A Fibre Channel ID, a 24-bit value unique within the address space of a fabric. The zero-length string value is used in circumstances in which the Fibre Channel ID is unassigned/unknown.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(3, 3), )
class Hh3cFcNameId(TextualConvention, OctetString):
    description = 'Represents the World Wide Name (WWN) associated with a Fibre Channel entity. A WWN is a 64-bit address to uniquely identify each entity within a Fibre Channel fabric.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class Hh3cFcNameIdOrZero(TextualConvention, OctetString):
    description = 'The World Wide Name (WWN) associated with a Fibre Channel entity. WWNs are initially defined as 64 bits in length. The latest definition (for future use) is 128 bits. The zero-length string value is used in circumstances in which the WWN is unassigned/unknown.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), )
class Hh3cFcClassOfServices(TextualConvention, Bits):
    description = 'Represents the class of service capability of an Nx_Port or Fx_Port.'
    status = 'current'
    namedValues = NamedValues(("classF", 0), ("class1", 1), ("class2", 2), ("class3", 3), ("class4", 4), ("class5", 5), ("class6", 6))

class Hh3cFcBbCredit(TextualConvention, Integer32):
    description = 'Represents the buffer-to-buffer credit of a port.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 32767)

class Hh3cFcRxMTU(TextualConvention, Integer32):
    description = 'Represents the maximum size of payload that a port can receive.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(128, 2112)

class Hh3cFcVsanIndex(TextualConvention, Unsigned32):
    description = 'Used as a unique index value to identify a particular VSAN (Virtual Storage Area Network).'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4095)

class Hh3cFcStartOper(TextualConvention, Integer32):
    description = 'Enable/disable an operation. enable - enable the operation. disable - disable the operation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class Hh3cFcDomainId(TextualConvention, Integer32):
    description = 'Represents the domain ID of the switch. Domain IDs can be assigned automatically by the principal switch or manually configured by the user.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 239)

class Hh3cFcDomainIdOrZero(TextualConvention, Integer32):
    description = 'Represents the domain ID of the switch. The zero value is used in circumstances in which the domain ID is unassigned/unknown.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 239)

class Hh3cFcDomainPriority(TextualConvention, Unsigned32):
    description = 'Priority of the switch which is used during principal switch selection to cause one Switch to befavored over another. The priority value for FC switches is in the range of 1 to 254. The smaller the value, the higher the priority.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 254)

class Hh3cFcDmState(TextualConvention, Integer32):
    description = 'Represents the state of domain: disabledWithNoDomain - initialling with domain configuration disabled and no manual domain configuration. disabledWithDomainCfg - initialling with configuration disabled and manual domain configuration. stableWithNoEports - stable with no E_Port UP. stableWithDomainCfg - stable with domain ID configured. stableWithNoDomain - stable with no domain ID configured. principalSwitchInSelect - progressing principal switch selection. domainIdRequesting - requesting for the domain ID. buildFabricPhase - processing building fabric. reconfigureFabricPhase - processing fabric reconfiguration. unknown - unknown state.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("disabledWithNoDomain", 1), ("disabledWithDomainCfg", 2), ("stableWithNoEports", 3), ("stableWithDomainCfg", 4), ("stableWithNoDomain", 5), ("principalSwitchInSelect", 6), ("domainIdRequesting", 7), ("buildFabricPhase", 8), ("reconfigureFabricPhase", 9), ("unknown", 10))

class Hh3cFcDomainIdList(TextualConvention, OctetString):
    description = "This object indicates the list of domain IDs that are allowed. Each octet within this value specifies a set of eight domains, with the first octet specifying domain ID through 1 through 8, the second octet specifying 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered ID, and the least significant bit represents the highest numbered ID. Thus, each domain ID of the VSAN is represented by a single bit within the value of this object. If that bit has a value of '1', then that domain ID is included, or else the domain ID is not included if its bit has a value of '0'. If this object has a value which is less than 32 bytes long, the domains not represented are not considered to be in the list. If this object has a value of zero-length, no domains will be allowed in this VSAN."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

mibBuilder.exportSymbols("HH3C-FC-TC-MIB", Hh3cFcAddressIdOrZero=Hh3cFcAddressIdOrZero, Hh3cFcNameIdOrZero=Hh3cFcNameIdOrZero, Hh3cFcDomainId=Hh3cFcDomainId, Hh3cFcAddressType=Hh3cFcAddressType, Hh3cFcVsanIndex=Hh3cFcVsanIndex, Hh3cFcAddressId=Hh3cFcAddressId, Hh3cFcBbCredit=Hh3cFcBbCredit, Hh3cFcDomainPriority=Hh3cFcDomainPriority, Hh3cFcAddress=Hh3cFcAddress, Hh3cFcDomainIdList=Hh3cFcDomainIdList, Hh3cFcRxMTU=Hh3cFcRxMTU, Hh3cFcDomainIdOrZero=Hh3cFcDomainIdOrZero, Hh3cFcDmState=Hh3cFcDmState, Hh3cFcClassOfServices=Hh3cFcClassOfServices, Hh3cFcStartOper=Hh3cFcStartOper, Hh3cFcNameId=Hh3cFcNameId)
