#
# PySNMP MIB module ELTEX-MES-DOT1X (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-DOT1X
# Produced by pysmi-0.3.4 at Wed May  1 13:01:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, NotificationType, MibIdentifier, ObjectIdentity, TimeTicks, Bits, iso, ModuleIdentity, IpAddress, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "MibIdentifier", "ObjectIdentity", "TimeTicks", "Bits", "iso", "ModuleIdentity", "IpAddress", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eltMesDot1x = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 95))
eltMesDot1x.setRevisions(('2015-08-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eltMesDot1x.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: eltMesDot1x.setLastUpdated('201508060000Z')
if mibBuilder.loadTexts: eltMesDot1x.setOrganization('Eltex Enterprise Co, Ltd.')
if mibBuilder.loadTexts: eltMesDot1x.setContactInfo('www.eltex.nsk.ru')
if mibBuilder.loadTexts: eltMesDot1x.setDescription("This private MIB module defines Eltex's private 802.1x MIBs.")
class Eltdot1xRadiusAttrNASPortFormatType(TextualConvention, Integer32):
    description = 'Specifies format of RADIUS NAS-Port option.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("default", 1), ("human", 2))

class Eltdot1xMacAuthFormatUsernameLettercase(TextualConvention, Integer32):
    description = 'String letter case type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("lowercase", 1), ("uppercase", 2))

class Eltdot1xMacAuthFormatUsernameSeparator(TextualConvention, Integer32):
    description = 'Chars separator type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("dash", 1), ("colon", 2), ("dot", 3))

class Eltdot1xMacAuthFormatUsernameGroupsize(TextualConvention, Integer32):
    description = 'Number of chars in a group.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 12))
    namedValues = NamedValues(("nibble", 1), ("byte", 2), ("word", 4), ("none", 12))

eltMesDot1xRadiusAttr = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 1))
eltdot1xRadiusAttrNASPortFormat = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 1, 1), Eltdot1xRadiusAttrNASPortFormatType().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltdot1xRadiusAttrNASPortFormat.setStatus('current')
if mibBuilder.loadTexts: eltdot1xRadiusAttrNASPortFormat.setDescription('RADIUS NAS-Port option format.')
eltMesDot1xMacAuth = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 2))
eltMesDot1xMacAuthFormat = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 2, 1))
eltdot1xMacAuthFormatUsernameLettercase = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 2, 1, 1), Eltdot1xMacAuthFormatUsernameLettercase()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltdot1xMacAuthFormatUsernameLettercase.setStatus('current')
if mibBuilder.loadTexts: eltdot1xMacAuthFormatUsernameLettercase.setDescription('Specifies the letter case of MAC address string contained in User-Name attribute (attribute 1) during MAC-based authentication.')
eltdot1xMacAuthFormatUsernameSeparator = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 2, 1, 2), Eltdot1xMacAuthFormatUsernameSeparator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltdot1xMacAuthFormatUsernameSeparator.setStatus('current')
if mibBuilder.loadTexts: eltdot1xMacAuthFormatUsernameSeparator.setDescription('Specifies the separator used in MAC address string contained in User-Name attribute (attribute 1) during MAC-based authentication.')
eltdot1xMacAuthFormatUsernameGroupsize = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 2, 1, 3), Eltdot1xMacAuthFormatUsernameGroupsize()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltdot1xMacAuthFormatUsernameGroupsize.setStatus('current')
if mibBuilder.loadTexts: eltdot1xMacAuthFormatUsernameGroupsize.setDescription('Specifies the number of chars in each group of MAC address string contained in User-Name attribute (attribute 1) during MAC-based authentication.')
eltdot1xMacAuthFormatUserPassword = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltdot1xMacAuthFormatUserPassword.setStatus('current')
if mibBuilder.loadTexts: eltdot1xMacAuthFormatUserPassword.setDescription("Specifies the string used in User-Password attribute (atribute 2) during MAC-based authentication instead of client's MAC-address.")
mibBuilder.exportSymbols("ELTEX-MES-DOT1X", Eltdot1xMacAuthFormatUsernameGroupsize=Eltdot1xMacAuthFormatUsernameGroupsize, eltdot1xMacAuthFormatUsernameLettercase=eltdot1xMacAuthFormatUsernameLettercase, Eltdot1xRadiusAttrNASPortFormatType=Eltdot1xRadiusAttrNASPortFormatType, eltdot1xMacAuthFormatUsernameSeparator=eltdot1xMacAuthFormatUsernameSeparator, Eltdot1xMacAuthFormatUsernameLettercase=Eltdot1xMacAuthFormatUsernameLettercase, eltMesDot1x=eltMesDot1x, eltMesDot1xMacAuthFormat=eltMesDot1xMacAuthFormat, Eltdot1xMacAuthFormatUsernameSeparator=Eltdot1xMacAuthFormatUsernameSeparator, PYSNMP_MODULE_ID=eltMesDot1x, eltdot1xRadiusAttrNASPortFormat=eltdot1xRadiusAttrNASPortFormat, eltdot1xMacAuthFormatUsernameGroupsize=eltdot1xMacAuthFormatUsernameGroupsize, eltdot1xMacAuthFormatUserPassword=eltdot1xMacAuthFormatUserPassword, eltMesDot1xMacAuth=eltMesDot1xMacAuth, eltMesDot1xRadiusAttr=eltMesDot1xRadiusAttr)
