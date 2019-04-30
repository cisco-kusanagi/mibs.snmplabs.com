#
# PySNMP MIB module ELTEX-MES-DOT1X (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-DOT1X
# Produced by pysmi-0.3.4 at Mon Apr 29 18:46:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, MibIdentifier, NotificationType, ObjectIdentity, Unsigned32, IpAddress, Counter64, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "MibIdentifier", "NotificationType", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter64", "Counter32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eltMesDot1x = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 95))
eltMesDot1x.setRevisions(('2015-08-06 00:00',))
if mibBuilder.loadTexts: eltMesDot1x.setLastUpdated('201508060000Z')
if mibBuilder.loadTexts: eltMesDot1x.setOrganization('Eltex Enterprise Co, Ltd.')
class Eltdot1xRadiusAttrNASPortFormatType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("default", 1), ("human", 2))

class Eltdot1xMacAuthFormatUsernameLettercase(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("lowercase", 1), ("uppercase", 2))

class Eltdot1xMacAuthFormatUsernameSeparator(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("dash", 1), ("colon", 2), ("dot", 3))

class Eltdot1xMacAuthFormatUsernameGroupsize(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 12))
    namedValues = NamedValues(("nibble", 1), ("byte", 2), ("word", 4), ("none", 12))

eltMesDot1xRadiusAttr = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 1))
eltdot1xRadiusAttrNASPortFormat = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 1, 1), Eltdot1xRadiusAttrNASPortFormatType().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltdot1xRadiusAttrNASPortFormat.setStatus('current')
eltMesDot1xMacAuth = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 2))
eltMesDot1xMacAuthFormat = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 2, 1))
eltdot1xMacAuthFormatUsernameLettercase = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 2, 1, 1), Eltdot1xMacAuthFormatUsernameLettercase()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltdot1xMacAuthFormatUsernameLettercase.setStatus('current')
eltdot1xMacAuthFormatUsernameSeparator = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 2, 1, 2), Eltdot1xMacAuthFormatUsernameSeparator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltdot1xMacAuthFormatUsernameSeparator.setStatus('current')
eltdot1xMacAuthFormatUsernameGroupsize = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 2, 1, 3), Eltdot1xMacAuthFormatUsernameGroupsize()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltdot1xMacAuthFormatUsernameGroupsize.setStatus('current')
eltdot1xMacAuthFormatUserPassword = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltdot1xMacAuthFormatUserPassword.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-DOT1X", eltMesDot1xMacAuthFormat=eltMesDot1xMacAuthFormat, eltdot1xMacAuthFormatUsernameSeparator=eltdot1xMacAuthFormatUsernameSeparator, eltdot1xMacAuthFormatUsernameGroupsize=eltdot1xMacAuthFormatUsernameGroupsize, eltdot1xMacAuthFormatUserPassword=eltdot1xMacAuthFormatUserPassword, PYSNMP_MODULE_ID=eltMesDot1x, Eltdot1xMacAuthFormatUsernameGroupsize=Eltdot1xMacAuthFormatUsernameGroupsize, Eltdot1xMacAuthFormatUsernameSeparator=Eltdot1xMacAuthFormatUsernameSeparator, eltdot1xRadiusAttrNASPortFormat=eltdot1xRadiusAttrNASPortFormat, eltMesDot1xRadiusAttr=eltMesDot1xRadiusAttr, eltMesDot1xMacAuth=eltMesDot1xMacAuth, eltdot1xMacAuthFormatUsernameLettercase=eltdot1xMacAuthFormatUsernameLettercase, Eltdot1xMacAuthFormatUsernameLettercase=Eltdot1xMacAuthFormatUsernameLettercase, eltMesDot1x=eltMesDot1x, Eltdot1xRadiusAttrNASPortFormatType=Eltdot1xRadiusAttrNASPortFormatType)
