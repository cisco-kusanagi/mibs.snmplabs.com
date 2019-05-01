#
# PySNMP MIB module CISCOSB-WeightedRandomTailDrop-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-WeightedRandomTailDrop-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:24:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibIdentifier, Counter64, ObjectIdentity, Counter32, Unsigned32, Gauge32, Integer32, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "Counter64", "ObjectIdentity", "Counter32", "Unsigned32", "Gauge32", "Integer32", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlWeightedRandomTailDrop = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 146))
rlWeightedRandomTailDrop.setRevisions(('2009-09-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlWeightedRandomTailDrop.setRevisionsDescriptions(('The private MIB module definition for Weighted Random Tail Drop MIB.',))
if mibBuilder.loadTexts: rlWeightedRandomTailDrop.setLastUpdated('200909290000Z')
if mibBuilder.loadTexts: rlWeightedRandomTailDrop.setOrganization('Cisco Small Business')
if mibBuilder.loadTexts: rlWeightedRandomTailDrop.setContactInfo('Postal: 170 West Tasman Drive San Jose , CA 95134-1706 USA Website: Cisco Small Business Home http://www.cisco.com/smb>;, Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlWeightedRandomTailDrop.setDescription('<description>')
rlWeightedRandomTailDropCurrentStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 146, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("enable", 0), ("disable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlWeightedRandomTailDropCurrentStatus.setStatus('current')
if mibBuilder.loadTexts: rlWeightedRandomTailDropCurrentStatus.setDescription('Show the current Weighted Random Tail Drop status')
rlWeightedRandomTailDropStatusAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 146, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("enable", 0), ("disable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlWeightedRandomTailDropStatusAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlWeightedRandomTailDropStatusAfterReset.setDescription('Set the Weighted Random Tail Drop status after reset')
mibBuilder.exportSymbols("CISCOSB-WeightedRandomTailDrop-MIB", rlWeightedRandomTailDropStatusAfterReset=rlWeightedRandomTailDropStatusAfterReset, rlWeightedRandomTailDrop=rlWeightedRandomTailDrop, PYSNMP_MODULE_ID=rlWeightedRandomTailDrop, rlWeightedRandomTailDropCurrentStatus=rlWeightedRandomTailDropCurrentStatus)
