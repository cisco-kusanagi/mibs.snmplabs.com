#
# PySNMP MIB module DEVEVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DEVEVENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:26:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
device, = mibBuilder.importSymbols("ANIROOT-MIB", "device")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter32, IpAddress, NotificationType, ModuleIdentity, Gauge32, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, Integer32, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "IpAddress", "NotificationType", "ModuleIdentity", "Gauge32", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "Integer32", "ObjectIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aniDevEvent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 2, 6))
if mibBuilder.loadTexts: aniDevEvent.setLastUpdated('0012111753Z')
if mibBuilder.loadTexts: aniDevEvent.setOrganization('Aperto Networks')
aniDevEvNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 4325, 2, 6, 2))
aniDevEmailSending = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 6, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevEmailSending.setStatus('current')
aniDevEmailSender = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 6, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevEmailSender.setStatus('current')
aniDevDomainName = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 6, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevDomainName.setStatus('current')
aniDevEmailReceiver1 = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 6, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevEmailReceiver1.setStatus('current')
aniDevEmailReceiver2 = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 6, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevEmailReceiver2.setStatus('current')
mibBuilder.exportSymbols("DEVEVENT-MIB", aniDevDomainName=aniDevDomainName, aniDevEmailSending=aniDevEmailSending, aniDevEmailReceiver1=aniDevEmailReceiver1, aniDevEmailReceiver2=aniDevEmailReceiver2, aniDevEvent=aniDevEvent, aniDevEmailSender=aniDevEmailSender, PYSNMP_MODULE_ID=aniDevEvent, aniDevEvNotify=aniDevEvNotify)
