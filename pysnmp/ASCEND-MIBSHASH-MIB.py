#
# PySNMP MIB module ASCEND-MIBSHASH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBSHASH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:12:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, Counter32, Counter64, Bits, Unsigned32, ObjectIdentity, TimeTicks, IpAddress, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "Counter32", "Counter64", "Bits", "Unsigned32", "ObjectIdentity", "TimeTicks", "IpAddress", "Gauge32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibsHashProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 108))
mibsHashProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 108, 1), )
if mibBuilder.loadTexts: mibsHashProfileTable.setStatus('mandatory')
mibsHashProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 108, 1, 1), ).setIndexNames((0, "ASCEND-MIBSHASH-MIB", "sHashProfile-Index-o"))
if mibBuilder.loadTexts: mibsHashProfileEntry.setStatus('mandatory')
sHashProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 108, 1, 1, 1), Integer32()).setLabel("sHashProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: sHashProfile_Index_o.setStatus('mandatory')
sHashProfile_Ipsec = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 108, 1, 1, 2), DisplayString()).setLabel("sHashProfile-Ipsec").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sHashProfile_Ipsec.setStatus('mandatory')
sHashProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 108, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("sHashProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sHashProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBSHASH-MIB", mibsHashProfileTable=mibsHashProfileTable, mibsHashProfileEntry=mibsHashProfileEntry, sHashProfile_Ipsec=sHashProfile_Ipsec, sHashProfile_Index_o=sHashProfile_Index_o, sHashProfile_Action_o=sHashProfile_Action_o, mibsHashProfile=mibsHashProfile, DisplayString=DisplayString)
