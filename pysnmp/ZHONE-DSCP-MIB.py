#
# PySNMP MIB module ZHONE-DSCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-DSCP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:41:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Gauge32, Counter64, Counter32, Unsigned32, iso, Integer32, NotificationType, MibIdentifier, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Gauge32", "Counter64", "Counter32", "Unsigned32", "iso", "Integer32", "NotificationType", "MibIdentifier", "Bits", "TimeTicks")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
zhoneIp, = mibBuilder.importSymbols("Zhone", "zhoneIp")
dscpProfile = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22))
if mibBuilder.loadTexts: dscpProfile.setLastUpdated('201006030603Z')
if mibBuilder.loadTexts: dscpProfile.setOrganization('Zhone Technologies, Inc.')
dscpProfileTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1), )
if mibBuilder.loadTexts: dscpProfileTable.setStatus('current')
dscpProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1), ).setIndexNames((0, "ZHONE-DSCP-MIB", "dscpIndex"))
if mibBuilder.loadTexts: dscpProfileEntry.setStatus('current')
dscpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: dscpIndex.setStatus('current')
dscpProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscpProfileRowStatus.setStatus('current')
dscp00map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp00map8021p.setStatus('current')
dscp01map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp01map8021p.setStatus('current')
dscp02map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp02map8021p.setStatus('current')
dscp03map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp03map8021p.setStatus('current')
dscp04map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp04map8021p.setStatus('current')
dscp05map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp05map8021p.setStatus('current')
dscp06map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp06map8021p.setStatus('current')
dscp07map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp07map8021p.setStatus('current')
dscp08map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp08map8021p.setStatus('current')
dscp09map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp09map8021p.setStatus('current')
dscp10map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp10map8021p.setStatus('current')
dscp11map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp11map8021p.setStatus('current')
dscp12map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp12map8021p.setStatus('current')
dscp13map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp13map8021p.setStatus('current')
dscp14map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp14map8021p.setStatus('current')
dscp15map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp15map8021p.setStatus('current')
dscp16map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp16map8021p.setStatus('current')
dscp17map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp17map8021p.setStatus('current')
dscp18map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp18map8021p.setStatus('current')
dscp19map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp19map8021p.setStatus('current')
dscp20map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp20map8021p.setStatus('current')
dscp21map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp21map8021p.setStatus('current')
dscp22map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp22map8021p.setStatus('current')
dscp23map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp23map8021p.setStatus('current')
dscp24map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp24map8021p.setStatus('current')
dscp25map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp25map8021p.setStatus('current')
dscp26map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 29), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp26map8021p.setStatus('current')
dscp27map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp27map8021p.setStatus('current')
dscp28map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 31), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp28map8021p.setStatus('current')
dscp29map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 32), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp29map8021p.setStatus('current')
dscp30map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 33), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp30map8021p.setStatus('current')
dscp31map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 34), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp31map8021p.setStatus('current')
dscp32map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 35), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp32map8021p.setStatus('current')
dscp33map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 36), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp33map8021p.setStatus('current')
dscp34map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 37), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp34map8021p.setStatus('current')
dscp35map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 38), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp35map8021p.setStatus('current')
dscp36map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 39), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp36map8021p.setStatus('current')
dscp37map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 40), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp37map8021p.setStatus('current')
dscp38map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 41), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp38map8021p.setStatus('current')
dscp39map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 42), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp39map8021p.setStatus('current')
dscp40map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 43), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp40map8021p.setStatus('current')
dscp41map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 44), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp41map8021p.setStatus('current')
dscp42map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 45), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp42map8021p.setStatus('current')
dscp43map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 46), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp43map8021p.setStatus('current')
dscp44map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 47), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp44map8021p.setStatus('current')
dscp45map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 48), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp45map8021p.setStatus('current')
dscp46map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 49), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp46map8021p.setStatus('current')
dscp47map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 50), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp47map8021p.setStatus('current')
dscp48map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 51), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp48map8021p.setStatus('current')
dscp49map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 52), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp49map8021p.setStatus('current')
dscp50map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 53), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp50map8021p.setStatus('current')
dscp51map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 54), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp51map8021p.setStatus('current')
dscp52map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 55), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp52map8021p.setStatus('current')
dscp53map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 56), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp53map8021p.setStatus('current')
dscp54map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 57), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp54map8021p.setStatus('current')
dscp55map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 58), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp55map8021p.setStatus('current')
dscp56map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 59), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp56map8021p.setStatus('current')
dscp57map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 60), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp57map8021p.setStatus('current')
dscp58map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 61), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp58map8021p.setStatus('current')
dscp59map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 62), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp59map8021p.setStatus('current')
dscp60map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 63), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp60map8021p.setStatus('current')
dscp61map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 64), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp61map8021p.setStatus('current')
dscp62map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 65), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp62map8021p.setStatus('current')
dscp63map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 66), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscp63map8021p.setStatus('current')
dscpProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 2)).setObjects(("ZHONE-DSCP-MIB", "dscpProfileRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dscpProfileGroup = dscpProfileGroup.setStatus('current')
dscpProfileGroupObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 3)).setObjects(("ZHONE-DSCP-MIB", "dscp00map8021p"), ("ZHONE-DSCP-MIB", "dscp01map8021p"), ("ZHONE-DSCP-MIB", "dscp02map8021p"), ("ZHONE-DSCP-MIB", "dscp03map8021p"), ("ZHONE-DSCP-MIB", "dscp04map8021p"), ("ZHONE-DSCP-MIB", "dscp05map8021p"), ("ZHONE-DSCP-MIB", "dscp06map8021p"), ("ZHONE-DSCP-MIB", "dscp07map8021p"), ("ZHONE-DSCP-MIB", "dscp08map8021p"), ("ZHONE-DSCP-MIB", "dscp09map8021p"), ("ZHONE-DSCP-MIB", "dscp10map8021p"), ("ZHONE-DSCP-MIB", "dscp11map8021p"), ("ZHONE-DSCP-MIB", "dscp12map8021p"), ("ZHONE-DSCP-MIB", "dscp13map8021p"), ("ZHONE-DSCP-MIB", "dscp14map8021p"), ("ZHONE-DSCP-MIB", "dscp15map8021p"), ("ZHONE-DSCP-MIB", "dscp16map8021p"), ("ZHONE-DSCP-MIB", "dscp17map8021p"), ("ZHONE-DSCP-MIB", "dscp18map8021p"), ("ZHONE-DSCP-MIB", "dscp19map8021p"), ("ZHONE-DSCP-MIB", "dscp20map8021p"), ("ZHONE-DSCP-MIB", "dscp21map8021p"), ("ZHONE-DSCP-MIB", "dscp22map8021p"), ("ZHONE-DSCP-MIB", "dscp23map8021p"), ("ZHONE-DSCP-MIB", "dscp24map8021p"), ("ZHONE-DSCP-MIB", "dscp25map8021p"), ("ZHONE-DSCP-MIB", "dscp26map8021p"), ("ZHONE-DSCP-MIB", "dscp27map8021p"), ("ZHONE-DSCP-MIB", "dscp28map8021p"), ("ZHONE-DSCP-MIB", "dscp29map8021p"), ("ZHONE-DSCP-MIB", "dscp30map8021p"), ("ZHONE-DSCP-MIB", "dscp31map8021p"), ("ZHONE-DSCP-MIB", "dscp32map8021p"), ("ZHONE-DSCP-MIB", "dscp33map8021p"), ("ZHONE-DSCP-MIB", "dscp34map8021p"), ("ZHONE-DSCP-MIB", "dscp35map8021p"), ("ZHONE-DSCP-MIB", "dscp36map8021p"), ("ZHONE-DSCP-MIB", "dscp37map8021p"), ("ZHONE-DSCP-MIB", "dscp38map8021p"), ("ZHONE-DSCP-MIB", "dscp39map8021p"), ("ZHONE-DSCP-MIB", "dscp40map8021p"), ("ZHONE-DSCP-MIB", "dscp41map8021p"), ("ZHONE-DSCP-MIB", "dscp42map8021p"), ("ZHONE-DSCP-MIB", "dscp43map8021p"), ("ZHONE-DSCP-MIB", "dscp44map8021p"), ("ZHONE-DSCP-MIB", "dscp45map8021p"), ("ZHONE-DSCP-MIB", "dscp46map8021p"), ("ZHONE-DSCP-MIB", "dscp47map8021p"), ("ZHONE-DSCP-MIB", "dscp48map8021p"), ("ZHONE-DSCP-MIB", "dscp49map8021p"), ("ZHONE-DSCP-MIB", "dscp50map8021p"), ("ZHONE-DSCP-MIB", "dscp51map8021p"), ("ZHONE-DSCP-MIB", "dscp52map8021p"), ("ZHONE-DSCP-MIB", "dscp53map8021p"), ("ZHONE-DSCP-MIB", "dscp54map8021p"), ("ZHONE-DSCP-MIB", "dscp55map8021p"), ("ZHONE-DSCP-MIB", "dscp56map8021p"), ("ZHONE-DSCP-MIB", "dscp57map8021p"), ("ZHONE-DSCP-MIB", "dscp58map8021p"), ("ZHONE-DSCP-MIB", "dscp59map8021p"), ("ZHONE-DSCP-MIB", "dscp60map8021p"), ("ZHONE-DSCP-MIB", "dscp61map8021p"), ("ZHONE-DSCP-MIB", "dscp62map8021p"), ("ZHONE-DSCP-MIB", "dscp63map8021p"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dscpProfileGroupObjectGroup = dscpProfileGroupObjectGroup.setStatus('current')
mibBuilder.exportSymbols("ZHONE-DSCP-MIB", dscp27map8021p=dscp27map8021p, dscp40map8021p=dscp40map8021p, dscp05map8021p=dscp05map8021p, dscp46map8021p=dscp46map8021p, dscp51map8021p=dscp51map8021p, dscp56map8021p=dscp56map8021p, dscp47map8021p=dscp47map8021p, dscp45map8021p=dscp45map8021p, dscp49map8021p=dscp49map8021p, dscp57map8021p=dscp57map8021p, dscp42map8021p=dscp42map8021p, dscp01map8021p=dscp01map8021p, dscp25map8021p=dscp25map8021p, dscp61map8021p=dscp61map8021p, dscp28map8021p=dscp28map8021p, dscp52map8021p=dscp52map8021p, dscp18map8021p=dscp18map8021p, dscp59map8021p=dscp59map8021p, dscp30map8021p=dscp30map8021p, dscp63map8021p=dscp63map8021p, dscp13map8021p=dscp13map8021p, dscp53map8021p=dscp53map8021p, dscpProfile=dscpProfile, dscpIndex=dscpIndex, dscp15map8021p=dscp15map8021p, dscp14map8021p=dscp14map8021p, dscp33map8021p=dscp33map8021p, dscpProfileEntry=dscpProfileEntry, dscp24map8021p=dscp24map8021p, dscp34map8021p=dscp34map8021p, dscp32map8021p=dscp32map8021p, dscp31map8021p=dscp31map8021p, dscp19map8021p=dscp19map8021p, dscp36map8021p=dscp36map8021p, dscp43map8021p=dscp43map8021p, dscp54map8021p=dscp54map8021p, dscp37map8021p=dscp37map8021p, dscp16map8021p=dscp16map8021p, dscp50map8021p=dscp50map8021p, dscp12map8021p=dscp12map8021p, dscpProfileTable=dscpProfileTable, dscp20map8021p=dscp20map8021p, dscp48map8021p=dscp48map8021p, dscp26map8021p=dscp26map8021p, dscp38map8021p=dscp38map8021p, dscpProfileGroup=dscpProfileGroup, dscp10map8021p=dscp10map8021p, dscp29map8021p=dscp29map8021p, dscp60map8021p=dscp60map8021p, dscpProfileGroupObjectGroup=dscpProfileGroupObjectGroup, dscp22map8021p=dscp22map8021p, dscp11map8021p=dscp11map8021p, dscp04map8021p=dscp04map8021p, dscpProfileRowStatus=dscpProfileRowStatus, dscp41map8021p=dscp41map8021p, dscp06map8021p=dscp06map8021p, dscp17map8021p=dscp17map8021p, dscp00map8021p=dscp00map8021p, dscp02map8021p=dscp02map8021p, dscp35map8021p=dscp35map8021p, dscp44map8021p=dscp44map8021p, dscp07map8021p=dscp07map8021p, dscp39map8021p=dscp39map8021p, dscp21map8021p=dscp21map8021p, dscp23map8021p=dscp23map8021p, dscp62map8021p=dscp62map8021p, PYSNMP_MODULE_ID=dscpProfile, dscp55map8021p=dscp55map8021p, dscp09map8021p=dscp09map8021p, dscp03map8021p=dscp03map8021p, dscp08map8021p=dscp08map8021p, dscp58map8021p=dscp58map8021p)
