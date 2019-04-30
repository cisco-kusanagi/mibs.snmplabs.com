#
# PySNMP MIB module Brocade-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Brocade-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 17:19:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
bcsiModules, = mibBuilder.importSymbols("Brocade-REG-MIB", "bcsiModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, NotificationType, TimeTicks, Counter32, MibIdentifier, iso, Bits, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "NotificationType", "TimeTicks", "Counter32", "MibIdentifier", "iso", "Bits", "ModuleIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bcsiModuleTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 1, 2))
bcsiModuleTC.setRevisions(('2003-01-13 14:30',))
if mibBuilder.loadTexts: bcsiModuleTC.setLastUpdated('200301131430Z')
if mibBuilder.loadTexts: bcsiModuleTC.setOrganization('Brocade Communications Systems, Inc.,')
class FcWwn(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class SwDomainIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 239)

class SwNbIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2048)

class SwSensorIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 1024)

class SwPortIndex(TextualConvention, Integer32):
    status = 'current'

class SwTrunkMaster(TextualConvention, Integer32):
    status = 'current'

mibBuilder.exportSymbols("Brocade-TC", SwPortIndex=SwPortIndex, SwDomainIndex=SwDomainIndex, FcWwn=FcWwn, SwTrunkMaster=SwTrunkMaster, SwNbIndex=SwNbIndex, bcsiModuleTC=bcsiModuleTC, PYSNMP_MODULE_ID=bcsiModuleTC, SwSensorIndex=SwSensorIndex)
