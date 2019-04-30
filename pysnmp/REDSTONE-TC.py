#
# PySNMP MIB module REDSTONE-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDSTONE-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 20:46:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rsMgmt, = mibBuilder.importSymbols("REDSTONE-SMI", "rsMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, MibIdentifier, Gauge32, ObjectIdentity, TimeTicks, NotificationType, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, Unsigned32, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "Gauge32", "ObjectIdentity", "TimeTicks", "NotificationType", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "Unsigned32", "iso", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rsTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 2773, 2, 1))
rsTextualConventions.setRevisions(('1998-01-01 00:00',))
if mibBuilder.loadTexts: rsTextualConventions.setLastUpdated('9801010000Z')
if mibBuilder.loadTexts: rsTextualConventions.setOrganization('Redstone Communications, Inc.')
class RsEnable(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disable", 0), ("enable", 1))

class RsName(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 15)

class RsNextIfIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class RsIpAddrLessIf(TextualConvention, IpAddress):
    status = 'current'

class RsTimeSlotMap(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class RsAcctngAdminType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class RsAcctngOperType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disable", 0), ("enable", 1), ("notSupported", 2))

mibBuilder.exportSymbols("REDSTONE-TC", RsAcctngOperType=RsAcctngOperType, rsTextualConventions=rsTextualConventions, RsAcctngAdminType=RsAcctngAdminType, RsName=RsName, PYSNMP_MODULE_ID=rsTextualConventions, RsEnable=RsEnable, RsIpAddrLessIf=RsIpAddrLessIf, RsNextIfIndex=RsNextIfIndex, RsTimeSlotMap=RsTimeSlotMap)
