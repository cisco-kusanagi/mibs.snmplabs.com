#
# PySNMP MIB module PERIBIT-GLOBAL-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PERIBIT-GLOBAL-TC
# Produced by pysmi-0.3.4 at Wed May  1 14:40:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
pnModules, = mibBuilder.importSymbols("PERIBIT-GLOBAL-REG", "pnModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, iso, Counter32, Bits, Counter64, Unsigned32, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "iso", "Counter32", "Bits", "Counter64", "Unsigned32", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "ObjectIdentity", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pnGlobalTcModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 1, 2))
pnGlobalTcModule.setRevisions(('2004-03-15 14:00', '2003-06-26 20:00', '2002-11-07 19:00', '2001-07-29 22:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pnGlobalTcModule.setRevisionsDescriptions((' Add sr100 chassis type.', ' Add sr80 chassis type.', ' Add sr20 chassis type.', ' Rev 1.0 Initial version of MIB module PERIBIT-GLOBAL-TC.',))
if mibBuilder.loadTexts: pnGlobalTcModule.setLastUpdated('200107292200Z')
if mibBuilder.loadTexts: pnGlobalTcModule.setOrganization('Peribit Networks, Inc')
if mibBuilder.loadTexts: pnGlobalTcModule.setContactInfo(' Customer Support Peribit Networks, Inc. 2300 Central Expressway Santa Clara, CA 95050 +1 866-PERIBIT support@peribit.com')
if mibBuilder.loadTexts: pnGlobalTcModule.setDescription(" A MIB module containing textual conventions for Peribit Networks' enterprise MIB modules. These textual conventions are used across all Peribit products.")
class TcAppName(TextualConvention, OctetString):
    description = " Represents the name of an application. This has all the restrictions of the DisplayString textual convention with the following additional ones: - Only the following characters/character ranges are allowed: 0-9 A-Z a-z :./#$&_-+()' <space> Any object defined using this syntax may not exceed 64 characters in length."
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class TcChassisType(TextualConvention, Integer32):
    description = ' Enumerates all possible chassis types for Peribit devices.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("pnOther", 1), ("pnSr50", 2), ("pnSr20", 3), ("pnSr80", 4), ("pnSr100", 5), ("pnSm500", 6), ("pnSr15", 7))

mibBuilder.exportSymbols("PERIBIT-GLOBAL-TC", pnGlobalTcModule=pnGlobalTcModule, TcChassisType=TcChassisType, PYSNMP_MODULE_ID=pnGlobalTcModule, TcAppName=TcAppName)
