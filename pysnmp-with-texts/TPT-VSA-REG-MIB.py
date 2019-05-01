#
# PySNMP MIB module TPT-VSA-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-VSA-REG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:26:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ModuleIdentity, Integer32, Counter32, NotificationType, Unsigned32, IpAddress, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "Integer32", "Counter32", "NotificationType", "Unsigned32", "IpAddress", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "iso", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tpt_reg, tpt_products = mibBuilder.importSymbols("TIPPINGPOINT-REG-MIB", "tpt-reg", "tpt-products")
tpt_vsaMIBs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 10)).setLabel("tpt-vsaMIBs")
tpt_vsaMIBs.setRevisions(('2016-05-25 18:54', '2014-11-11 19:37',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tpt_vsaMIBs.setRevisionsDescriptions(('Updated copyright information. Minor MIB syntax fixes.', 'Initial version.',))
if mibBuilder.loadTexts: tpt_vsaMIBs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_vsaMIBs.setOrganization('Trend Micro, Inc.')
if mibBuilder.loadTexts: tpt_vsaMIBs.setContactInfo('www.trendmicro.com')
if mibBuilder.loadTexts: tpt_vsaMIBs.setDescription("Sub-tree for TippingPoint Virtual Security Appliance (VSA) objects. Copyright (C) 2016 Trend Micro Incorporated. All Rights Reserved. Trend Micro makes no warranty of any kind with regard to this material, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. Trend Micro shall not be liable for errors contained herein or for incidental or consequential damages in connection with the furnishing, performance, or use of this material. This document contains proprietary information, which is protected by copyright. No part of this document may be photocopied, reproduced, or translated into another language without the prior written consent of Trend Micro. The information is provided 'as is' without warranty of any kind and is subject to change without notice. The only warranties for Trend Micro products and services are set forth in the express warranty statements accompanying such products and services. Nothing herein should be construed as constituting an additional warranty. Trend Micro shall not be liable for technical or editorial errors or omissions contained herein. TippingPoint(R), the TippingPoint logo, and Digital Vaccine(R) are registered trademarks of Trend Micro. All other company and product names may be trademarks of their respective holders. All rights reserved. This document contains confidential information, trade secrets or both, which are the property of Trend Micro. No part of this documentation may be reproduced in any form or by any means or used to make any derivative work (such as translation, transformation, or adaptation) without written permission from Trend Micro or one of its subsidiaries. All other company and product names may be trademarks of their respective holders. ")
tpt_vsa_family = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10)).setLabel("tpt-vsa-family")
if mibBuilder.loadTexts: tpt_vsa_family.setStatus('current')
if mibBuilder.loadTexts: tpt_vsa_family.setDescription("Registration of TippingPoint's Virtual Security Appliance (VSA) product family.")
tpt_model_V10F = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10, 1)).setLabel("tpt-model-V10F")
if mibBuilder.loadTexts: tpt_model_V10F.setStatus('current')
if mibBuilder.loadTexts: tpt_model_V10F.setDescription('Registration for TippingPoint V10F vCloudSecure Virtual Appliance.')
tpt_model_V1000F = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10, 2)).setLabel("tpt-model-V1000F")
if mibBuilder.loadTexts: tpt_model_V1000F.setStatus('current')
if mibBuilder.loadTexts: tpt_model_V1000F.setDescription('Registration for TippingPoint V1000F vCloudSecure Virtual Appliance.')
tpt_model_V2000F = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10, 3)).setLabel("tpt-model-V2000F")
if mibBuilder.loadTexts: tpt_model_V2000F.setStatus('current')
if mibBuilder.loadTexts: tpt_model_V2000F.setDescription('Registration for TippingPoint V2000F vCloudSecure Virtual Appliance.')
tpt_model_V5000F = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10, 4)).setLabel("tpt-model-V5000F")
if mibBuilder.loadTexts: tpt_model_V5000F.setStatus('current')
if mibBuilder.loadTexts: tpt_model_V5000F.setDescription('Registration for TippingPoint V5000F vCloudSecure Virtual Appliance.')
mibBuilder.exportSymbols("TPT-VSA-REG-MIB", tpt_model_V2000F=tpt_model_V2000F, PYSNMP_MODULE_ID=tpt_vsaMIBs, tpt_vsaMIBs=tpt_vsaMIBs, tpt_model_V10F=tpt_model_V10F, tpt_model_V1000F=tpt_model_V1000F, tpt_vsa_family=tpt_vsa_family, tpt_model_V5000F=tpt_model_V5000F)
