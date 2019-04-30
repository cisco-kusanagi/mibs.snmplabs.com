#
# PySNMP MIB module CISCO-DMN-DSG-BISS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-BISS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:37:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, MibIdentifier, Counter32, ObjectIdentity, IpAddress, Unsigned32, ModuleIdentity, NotificationType, Gauge32, Counter64, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "MibIdentifier", "Counter32", "ObjectIdentity", "IpAddress", "Unsigned32", "ModuleIdentity", "NotificationType", "Gauge32", "Counter64", "iso", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGBISS = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38))
ciscoDSGBISS.setRevisions(('2010-08-02 07:00',))
if mibBuilder.loadTexts: ciscoDSGBISS.setLastUpdated('201008020700Z')
if mibBuilder.loadTexts: ciscoDSGBISS.setOrganization('Cisco Systems, Inc.')
bissMode = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mode1", 1), ("modeE", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bissMode.setStatus('current')
bissMode1SessionWord = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 13))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bissMode1SessionWord.setStatus('current')
bissModeESessionWord = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bissModeESessionWord.setStatus('current')
bissModeEInjectedId = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bissModeEInjectedId.setStatus('current')
mibBuilder.exportSymbols("CISCO-DMN-DSG-BISS-MIB", bissMode1SessionWord=bissMode1SessionWord, bissModeEInjectedId=bissModeEInjectedId, bissMode=bissMode, ciscoDSGBISS=ciscoDSGBISS, PYSNMP_MODULE_ID=ciscoDSGBISS, bissModeESessionWord=bissModeESessionWord)
