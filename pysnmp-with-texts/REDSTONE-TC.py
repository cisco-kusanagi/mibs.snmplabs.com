#
# PySNMP MIB module REDSTONE-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDSTONE-TC
# Produced by pysmi-0.3.4 at Wed May  1 14:55:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
rsMgmt, = mibBuilder.importSymbols("REDSTONE-SMI", "rsMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, ModuleIdentity, NotificationType, ObjectIdentity, MibIdentifier, Counter32, iso, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "ModuleIdentity", "NotificationType", "ObjectIdentity", "MibIdentifier", "Counter32", "iso", "Bits", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rsTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 2773, 2, 1))
rsTextualConventions.setRevisions(('1998-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsTextualConventions.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: rsTextualConventions.setLastUpdated('9801010000Z')
if mibBuilder.loadTexts: rsTextualConventions.setOrganization('Redstone Communications, Inc.')
if mibBuilder.loadTexts: rsTextualConventions.setContactInfo(' Redstone Communications, Inc. 5 Carlisle Road Westford MA 01886 USA Tel: +1-978-692-1999 Email: mib@redstonecom.com ')
if mibBuilder.loadTexts: rsTextualConventions.setDescription('Textual conventions defined and used by the Redstone Communications Inc. enterprise.')
class RsEnable(TextualConvention, Integer32):
    description = "Enterprise-standard SYNTAX for MIB objects having enumerated value pair 'enable' and 'disable'. Used for both admin (configurable) and oper (read-only) objects."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disable", 0), ("enable", 1))

class RsName(DisplayString):
    description = 'A text name of restricted length.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 15)

class RsNextIfIndex(TextualConvention, Integer32):
    description = 'Coordinate ifIndex value allocation for entries in an associated ifIndex-ed interface table, by first reading an ifIndex value from this object, then creating an entry, having that ifIndex value, in the associated interface table. The DESCRIPTION clause for an object of this type must identify the associated interface table. A GET of this object returns the next available ifIndex value to be used to create an entry in the associated interface table; or zero, if no valid ifIndex value is available. This object also returns a value of zero when it is the lexicographic successor of a varbind presented in an SNMP GETNEXT or GETBULK request, for which circumstance it is assumed that ifIndex allocation is unintended. Successive GETs will typically return different values, thus avoiding collisions among cooperating management clients seeking to create table entries simultaneously. Unless specified otherwise by its MAX-ACCESS and DESCRIPTION clauses, an object of this type is read-only, and a SET of such an object returns a notWritable error. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class RsIpAddrLessIf(TextualConvention, IpAddress):
    description = "Compressed index representation to identify both numbered and unnumbered ('address-less') IP subnetworks. One approach is to identify such interfaces with a 2-tuple consisting of <IpAddress, ifIndex>, where only one of the pair is nonzero for a valid interface (IpAddress is nonzero for numbered interfaces, ifIndex is nonzero for unnumbered interfaces). As an alternative, this textual convention compresses the 2-tuple information into an IpAddress (32-bit) format a.b.c.d having the following interpretation: Format Interpretation IP Interface Type -------------------------------------------------------------- 0.0.0.0 'null' value 'none' or 'wildcard', etc. a.b.c.d, a != 0 IP Address Numbered 0.b.c.d ifIndex Unnumbered For the unnumbered case, the value of the ifIndex is given by (b * 65536) + (c * 256) + (d) A side-effect of this approach is that ifIndex values for IP network interfaces must fall in the range 1..16777215 (i.e. 24 bits). "
    status = 'current'

class RsTimeSlotMap(TextualConvention, OctetString):
    description = 'A bit map representing one or more timeslots of a DS1/E1 interface. Bits are numbered in descending order from 31-0 starting from the most significant bit of the first octet and ending with the least significant bit of the fourth octet. Bits 1-24 are relevant for DS1 interfaces, bits 0-31 are relevant for E1 interfaces. A bit is set if the associated timeslot is in use, and cleared if the associated timeslot is not in use.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class RsAcctngAdminType(TextualConvention, Integer32):
    description = 'The desired administrative state for the collection of accounting records. The administrative domain governed by an object of RsAcctngAdminType is defined in the MIB OBJECT description that uses this type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class RsAcctngOperType(TextualConvention, Integer32):
    description = 'The operational state for the collection of accounting records. The administrative domain that an object of this type is reporting state for, is defined in the MIB object description that uses this type. The notSupported(2) state indicates that accounting data collection is not supported for the entity using an object of RsAcctngOperType type. If an entity does not support accounting data collection, an object of RsAcctngOperType type will report notSupported(2) regardless of the value set in the corresponding RsAcctngAdminType. The disabled(0) state indicates that the corresponding RsAcctngAdminType object has been set to disabled(0). If a data collection is in process, the value of RsAcctngOperType will change to disabled(0) after the current collection completes. The enabled(1) state indicates that the corresponding RsAcctngAdminType object has been set to enabled(1) and that the entity is ready to collect accounting records.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disable", 0), ("enable", 1), ("notSupported", 2))

mibBuilder.exportSymbols("REDSTONE-TC", RsName=RsName, RsAcctngOperType=RsAcctngOperType, RsIpAddrLessIf=RsIpAddrLessIf, RsTimeSlotMap=RsTimeSlotMap, PYSNMP_MODULE_ID=rsTextualConventions, RsNextIfIndex=RsNextIfIndex, rsTextualConventions=rsTextualConventions, RsEnable=RsEnable, RsAcctngAdminType=RsAcctngAdminType)
